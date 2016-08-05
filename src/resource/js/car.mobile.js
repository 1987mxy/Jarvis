/**
 * 
 */

$(function(){
	var neckDirectOptions = {
				e: {
					upDown: function () {return neckKeyDown('up');},
					downDown: function () {return neckKeyDown('down');},
					leftDown: function () {return neckKeyDown('left');},
					rightDown: function () {return neckKeyDown('right');},
					upUp: function () {return neckKeyUp('up');},
					downUp: function () {return neckKeyUp('down');},
					leftUp: function () {return neckKeyUp('left');},
					rightUp: function () {return neckKeyUp('right');}
				},
				isMobile: true
		},
		$neckDirect = direct().init('neck', neckDirectOptions);
	$neckDirect.addClass('pull-left').appendTo('#joystick');
	
	var footDirectOptions = {
				e: {
					upDown: function () {return footKeyDown('front');},
					downDown: function () {return footKeyDown('rear');},
					leftDown: function () {return footKeyDown('left');},
					rightDown: function () {return footKeyDown('right');},
					upUp: function () {return footKeyUp('front');},
					downUp: function () {return footKeyUp('rear');},
					leftUp: function () {return footKeyUp('left');},
					rightUp: function () {return footKeyUp('right');}
				},
				isMobile: true
		},
		$footDirect = direct().init('foot', footDirectOptions);
	$footDirect.addClass('pull-right').appendTo('#joystick');
	$('#neckReset').on({
		vclick: function () {
			runNeck('reset');
		}
	});
	
	resetEye();
});