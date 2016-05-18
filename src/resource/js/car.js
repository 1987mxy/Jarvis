/**
 * 
 */

// up,38
// down,40
// left,37
// right,39
var directKeyCode = {
	38 : 'neckUp',
	40 : 'neckDown',
	37 : 'neckLeft',
	39 : 'neckRight',
	
	87 : 'footUp',		//w
	83 : 'footDown',	//s
	65 : 'footLeft',	//a
	68 : 'footRight'	//d
};

var xNeckLock = '',
	yNeckLock = '',
	xFootLock = '',
	yFootLock = '';
$(function() {
	$(document).keydown(function(event) {
		direct = directKeyCode[event.which];
		//neck
		if ((direct == 'neckLeft' || direct == 'neckRight') && xNeckLock == '') {
			$('#' + direct).button('toggle').mousedown();
			xNeckLock = direct;
		} else if ((direct == 'neckUp' || direct == 'neckDown') && yNeckLock == '') {
			$('#' + direct).button('toggle').mousedown();
			yNeckLock = direct;
		}
		//foot
		else if ((direct == 'footLeft' || direct == 'footRight') && xFootLock == '') {
			$('#' + direct).button('toggle').mousedown();
			xFootLock = direct;
		} else if ((direct == 'footUp' || direct == 'footDown') && yFootLock == '') {
			$('#' + direct).button('toggle').mousedown();
			yFootLock = direct;
		}
	}).keyup(function(event) {
		direct = directKeyCode[event.which];
		//neck
		if ((direct == 'neckLeft' || direct == 'neckRight') && xNeckLock == direct) {
			$('#' + direct).button('toggle').mouseup();
			xNeckLock = '';
		} else if ((direct == 'neckUp' || direct == 'neckDown') && yNeckLock == direct) {
			$('#' + direct).button('toggle').mouseup();
			yNeckLock = '';
		}
		//foot
		else if ((direct == 'footLeft' || direct == 'footRight') && xFootLock == direct) {
			$('#' + direct).button('toggle').mouseup();
			xFootLock = '';
		} else if ((direct == 'footUp' || direct == 'footDown') && yFootLock == direct) {
			$('#' + direct).button('toggle').mouseup();
			yFootLock = '';
		}
	});

	$('.neck-direct-btn').mousedown(function() {
		runNeck($(this).attr('direct'));
	}).mouseup(function() {
		var direct = $(this).attr('id')
		stopNeck((direct == 'neckLeft' || direct == 'neckRight') ? 'x' : 'y');
	});
	
	$('.foot-direct-btn').mousedown(function() {
		runFoot($(this).attr('direct'));
	}).mouseup(function() {
		stopFoot();
	});
});