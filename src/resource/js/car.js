/**
 * 
 */

$(function(){
	var xNeckLock = '',
		yNeckLock = '',
		neckPrefix = 'neck-',
		neckDown = function (direct) {
			if ((direct == 'left' || direct == 'right') && xNeckLock == '') {
				xNeckLock = neckPrefix + direct;
				runNeck(direct);
				return true;
			} else if ((direct == 'up' || direct == 'down') && yNeckLock == '') {
				yNeckLock = neckPrefix + direct;
				runNeck(direct);
				return true;
			}
			return false;
		},
		neckUp = function (direct) {
			if ((direct == 'left' || direct == 'right') && xNeckLock == neckPrefix + direct) {
				stopNeck('x');
				xNeckLock = '';
				return true;
			} else if ((direct == 'up' || direct == 'down') && yNeckLock == neckPrefix + direct) {
				stopNeck('y');
				yNeckLock = '';
				return true;
			}
			return false;
		},
		$neckDirect = direct().init('neck', {
			upDown: function () {return neckDown('up');},
			downDown: function () {return neckDown('down');},
			leftDown: function () {return neckDown('left');},
			rightDown: function () {return neckDown('right');},
			upUp: function () {return neckUp('up');},
			downUp: function () {return neckUp('down');},
			leftUp: function () {return neckUp('left');},
			rightUp: function () {return neckUp('right');}
		}, {
			//9 : 'rest',		//tab
			87 : 'up',		//w
			83 : 'down',	//s
			65 : 'left',	//a
			68 : 'right'	//d
		});
	$neckDirect.addClass('pull-left').appendTo('#joystick');
	
	var footLock = '',
		footPrefix = 'foot-',
		footDown = function (direct) {
			if ((direct == 'front' ||
					direct == 'rear' ||
					direct == 'left' ||
					direct == 'right') && footLock == '') {
				footLock = footPrefix + direct;
				runFoot(direct);
				return true;
			}
			return false;
		},
		footUp = function (direct) {
			if (footLock == footPrefix + direct) {
				stopFoot();
				footLock = '';
				return true;
			}
			return false;
		},
		$footDirect = direct().init('foot', {
			upDown: function () {return footDown('front');},
			downDown: function () {return footDown('rear');},
			leftDown: function () {return footDown('left');},
			rightDown: function () {return footDown('right');},
			upUp: function () {return footUp('front');},
			downUp: function () {return footUp('rear');},
			leftUp: function () {return footUp('left');},
			rightUp: function () {return footUp('right');}
		}, {
			38 : 'up',			//up
			40 : 'down',		//down
			37 : 'left',		//left
			39 : 'right',		//right
		});
	$footDirect.addClass('pull-right').appendTo('#joystick');
});