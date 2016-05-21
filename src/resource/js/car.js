/**
 * 
 */

// up,38
// down,40
// left,37
// right,39
var directKeyCode = {
	38 : 'footFront',
	40 : 'footRear',
	37 : 'footLeft',
	39 : 'footRight',
	
	27 : 'neckRest',	//esc
	87 : 'neckUp',		//w
	83 : 'neckDown',	//s
	65 : 'neckLeft',	//a
	68 : 'neckRight'	//d
};

var xNeckLock = '',
	yNeckLock = '',
	footLock = '';
$(function() {
	$(document).keydown(function(event) {
		direct = directKeyCode[event.which];
		//neck
		if ((direct == 'neckLeft' || direct == 'neckRight') && xNeckLock == '') {
			xNeckLock = direct;
			if (direct == 'neckLeft') {
				neckDirect = 'left';
			} else if (direct == 'neckRight') {
				neckDirect = 'right';
			}
			runNeck(neckDirect);
		} else if ((direct == 'neckUp' || direct == 'neckDown') && yNeckLock == '') {
			yNeckLock = direct;
			if (direct == 'neckUp') {
				neckDirect = 'up';
			} else if (direct == 'neckDown') {
				neckDirect = 'down';
			}
			runNeck(neckDirect);
		} else if (direct == 'neckRest' && xNeckLock == '' && yNeckLock == '') {
			xNeckLock = yNeckLock = neckDirect = 'reset';
			runNeck(neckDirect);
		}
		//foot
		else if ((direct == 'footLeft' || direct == 'footRight') && footLock == '') {
			footLock = direct;
			if (direct == 'footLeft') {
				footDirect = 'left';
			} else if (direct == 'footRight') {
				footDirect = 'right';
			}
			runFoot(footDirect);
		} else if ((direct == 'footFront' || direct == 'footRear') && footLock == '') {
			footLock = direct;
			if (direct == 'footFront') {
				footDirect = 'front';
			} else if (direct == 'footRear') {
				footDirect = 'rear';
			}
			runFoot(footDirect);
		}
	}).keyup(function(event) {
		direct = directKeyCode[event.which];
		//neck
		if ((direct == 'neckLeft' || direct == 'neckRight') && xNeckLock == direct) {
			stopNeck('x');
			xNeckLock = '';
		} else if ((direct == 'neckUp' || direct == 'neckDown') && yNeckLock == direct) {
			stopNeck('y');
			yNeckLock = '';
		} else if (direct == 'neckRest' && xNeckLock != '' && yNeckLock != '') {
			xNeckLock = '';
			yNeckLock = '';
		}
		//foot
		else if ((direct == 'footLeft' ||
					direct == 'footRight' ||
					direct == 'footFront' ||
					direct == 'footRear') && footLock == direct) {
			stopFoot();
			footLock = '';
		}
	});
});