/**
 * 
 */

// up,38
// down,40
// left,37
// right,39
var directKeyCode = {
	38 : 'up',
	40 : 'down',
	37 : 'left',
	39 : 'right'
};

var xLock = '';
var yLock = '';
$(function() {
	$(document).keydown(function(event) {
		direct = directKeyCode[event.which];
		if ((direct == 'left' || direct == 'right') && xLock == '') {
			$('#' + direct).button('toggle').mousedown();
			xLock = direct;
		} else if ((direct == 'up' || direct == 'down') && yLock == '') {
			$('#' + direct).button('toggle').mousedown();
			yLock = direct;
		}
	}).keyup(function(event) {
		direct = directKeyCode[event.which];
		if ((direct == 'left' || direct == 'right') && xLock == direct) {
			$('#' + direct).button('toggle').mouseup();
			xLock = '';
		} else if ((direct == 'up' || direct == 'down') && yLock == direct) {
			$('#' + direct).button('toggle').mouseup();
			yLock = '';
		}
	});

	$('.direct-btn').mousedown(function() {
		run($(this).attr('id'));
	}).mouseup(function() {
		var direct = $(this).attr('id')
		stop((direct == 'left' || direct == 'right') ? 'x' : 'y');
	});
});