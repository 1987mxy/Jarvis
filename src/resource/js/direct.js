/**
 * 方向控件
 */

function direct () {
	var tpl = '<div class="direct">' +
					'<div class="row">' +
						'<div class="up pull-right">' +
							'<div class="fs1 direct-btn" aria-hidden="true" data-op="up" data-icon="&#x3a;" data-up="&#x3a;" data-down="&#xe043;"></div>' +
						'</div>' +
					'</div>' +
					'<div class="row">' +
						'<div class="left pull-left">' +
							'<div class="fs1 direct-btn" aria-hidden="true" data-op="left" data-icon="&#x3c;" data-up="&#x3c;" data-down="&#xe045;"></div>' +
						'</div>' +
						'<div class="right pull-right">' +
							'<div class="fs1 direct-btn" aria-hidden="true" data-op="right" data-icon="&#x3d;" data-up="&#x3d;" data-down="&#xe046;"></div>' +
						'</div>' +
					'</div>' +
					'<div class="row">' +
						'<div class="down pull-right">' +
							'<div class="fs1 direct-btn" aria-hidden="true" data-op="down" data-icon="&#x3b;" data-up="&#x3b;" data-down="&#xe044;"></div>' +
						'</div>' +
					'</div>' +
				'</div>';
	var dom = {
		btn: '.direct-btn'
	};
	
	var directList = [];
	
	var event = {
		init: function (name, e, keyBind) {
			if (directList[name] == undefined) {
				directList[name] = $(tpl).clone();
			}
			directList[name].on({
				mousedown: function () {
					e[$(this).data('op') + 'Down']() &&
					$(this).attr('data-icon', $(this).data('down'));
				},
				mouseup: function () {
					e[$(this).data('op') + 'Up']() &&
					$(this).attr('data-icon', $(this).data('up'));
				},
			}, dom.btn);
			if (typeof keyBind != 'undefined') {
				$(document).on({
					keydown: function (event) {
						direct = keyBind[event.which];
						direct != undefined && directList[name].find(dom.btn + '[data-op="' + direct + '"]').mousedown();
					},
					keyup: function (event) {
						direct = keyBind[event.which];
						direct != undefined && directList[name].find(dom.btn + '[data-op="' + direct + '"]').mouseup();
					}
				});
			}
			return directList[name];
		}
	};
	
	return event;
};