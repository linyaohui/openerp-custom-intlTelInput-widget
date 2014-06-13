openerp.web_intlTelInput_widget = function(instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;
	instance.web_intlTelInput_widget = {};
	instance.web_intlTelInput_widget.intlTelInput = instance.web.form.AbstractField.extend({
		
			init: function() {
				this._super.apply(this, arguments);
				this.set("value", "");
			},
			start: function() {
				this.on("change:effective_readonly", this, function() {
					this.display_field();
					this.render_value();
				});
				this.display_field();
				return this._super();
			},
			display_field: function() {
				var self = this;
				this.$el.html(QWeb.render("intlTelInput", {widget: this}));
				if (! this.get("effective_readonly")) {
					this.$(".mobile-number").change(function() {
						self.internal_set_value(self.$(".mobile-number").val());
					});
				}
			},
			render_value: function() {
				if (this.get("effective_readonly")) {
					$(".mobile-number").val(this.get("value"));
					//this._super();
				} else {
					$(".mobile-number").val(this.get("value")||'').intlTelInput();
				}
		},
	  
});

 instance.web.form.widgets.add('intlTelInput', 'instance.web_intlTelInput_widget.intlTelInput');
}