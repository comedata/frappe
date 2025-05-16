import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    """
    在提交文档之前，根据交易类型执行验证和状态更新。
    """

    def before_submit(self):
        # 如果交易类型是"Issue"（借阅），执行借阅验证并更新文章状态为"Issued"（已借出）
        if self.type == "Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            # 将图书状态设置为已借出
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        # 如果交易类型是"Return"（归还），执行归还验证并更新文章状态为"Available"（可用）
        elif self.type == "Return":
            self.validate_return()
            # 将图书状态设置为可用
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    """
    验证图书是否可以借阅。
    """

    def validate_issue(self):
        # 先验证会员是否有有效会籍
        self.validate_membership()
        # 获取当前图书对象
        article = frappe.get_doc("Article", self.article)
        # 如果图书状态已经是“Issued”（已借出），抛出异常
        if article.status == "Issued":
            frappe.throw("该图书已被其他会员借出")

    """
    验证图书是否可以归还。
    """

    def validate_return(self):
        # 获取当前图书对象
        article = frappe.get_doc("Article", self.article)
        # 如果图书状态是“Available”（可用），说明未被借出，无法归还
        if article.status == "Available":
            frappe.throw("图书在未被借出的情况下不能归还")
            
    def validate_maximum_limit(self):
    # 从系统设置中获取允许借阅的最大图书数量
        print("已执行+++++++",self.name)
        max_articles = frappe.db.get_single_value("Library Settings", "maximum_number_of_issued_articles")

        # 查询当前会员已经成功提交的借阅记录数量
        count = frappe.db.count(
			"Library Transaction",
			{
				"library_member": self.library_member,   # 当前会员ID
				"type": "Issue",                         # 只统计借阅类型的交易
				"docstatus": DocStatus.submitted(),      # 仅统计已提交的有效交易
			},
		)

    # 如果当前借阅数量已经达到或超过系统设定的最大值，则抛出异常，阻止继续借阅
        if count >= max_articles:
            frappe.throw("该会员借阅图书数量已达上限")


    """
    验证会员是否有有效的会籍。
    """

    def validate_membership(self):
        # 检查是否存在该会员的有效会籍记录
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,  # 会员ID
                "docstatus": DocStatus.submitted(),     # 文档状态必须为已提交
                "from_date": ("=<", self.date),          # 当前日期应在会籍起始日期之后
                "to_date": (">=", self.date),            # 当前日期也应在会籍结束日期之前
            },
        )
        # 如果没有找到有效会籍，抛出异常
        if not valid_membership:
            frappe.throw("该会员没有有效会籍")