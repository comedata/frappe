# Copyright (c) 2025, ljack and contributors
# For license information, please see license.txt

# 导入 frappe 模块（当前被注释掉）
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMembership(Document):
    """
    LibraryMembership 类继承自 Document。
    此类用于处理图书馆会员资格相关的操作。
    """
    
    # 提交文档前执行的方法
    def before_submit(self):
        """
        在提交此会员资格文档之前，检查该图书馆成员是否已有有效的会员资格。
        
        如果已经存在有效会员资格，则抛出异常，提示不应提交新的会员资格。
        """
        # 查询是否存在当前成员的已提交且有效期覆盖新会员资格起始日期的会员记录
        exists = frappe.db.exists(
            "Library Membership",  # 文档类型名称
            {
                "library_member": self.library_member,  # 当前会员成员
                "docstatus": DocStatus.submitted(),  # 已提交状态
                # 检查现有会员资格的结束日期是否晚于当前会员资格的开始日期
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            # 如果存在冲突的会员资格，抛出异常提示用户
            frappe.throw("该成员已有有效的会员资格")
        
		# 获取贷款期限，并通过将贷款期限加到起始日期上来计算到期日期
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)