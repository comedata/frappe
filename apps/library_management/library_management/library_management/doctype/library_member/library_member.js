frappe.ui.form.on('Library Member', {
    refresh: function (frm) {
        // 创建会员按钮 - 浅绿色背景
        frm.add_custom_button(__('创建会员'), () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        }).css("background-color", "#E8F5E9"); // 浅绿色背景

        // 创建订单按钮 - 浅蓝色背景
        frm.add_custom_button(__('创建订单'), () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            });
        }).css("background-color", "#E3F2FD"); // 浅蓝色背景
    }
});