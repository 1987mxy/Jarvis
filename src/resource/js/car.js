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
				keyBind: {
					87 : 'up',		//w
					83 : 'down',	//s
					65 : 'left',	//a
					68 : 'right'	//d
				}
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
				keyBind: {
					38 : 'up',			//up
					40 : 'down',		//down
					37 : 'left',		//left
					39 : 'right',		//right
				}
		},
		$footDirect = direct().init('foot', footDirectOptions);
	$footDirect.addClass('pull-right').appendTo('#joystick');
	$('#neckReset').click(function(){runNeck('reset');});
	$(document).keyup(function (event) {
		//blank space
		event.which == 32 && runNeck('reset');
	});
});