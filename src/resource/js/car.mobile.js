/**
 * 
 */

var lock = 'x';
$(function() {
	// $('.direct-btn').touchstart(function() {
	// 	var direct = $(this).attr('id');
	// 	if ((direct == 'left' || direct == 'right') && xLock == '') {
	// 		$(this).button('toggle');
	// 		run(direct);
	// 		xLock = direct;
	// 	} else if ((direct == 'up' || direct == 'down') && yLock == '') {
	// 		$(this).button('toggle');
	// 		run(direct);
	// 		yLock = direct;
	// 	}
	// }).touchend(function() {
	// 	var direct = $(this).attr('id');
	// 	if ((direct == 'left' || direct == 'right') && xLock == direct) {
	// 		$(this).button('toggle');
	// 		stop(direct);
	// 		xLock = '';
	// 	} else if ((direct == 'up' || direct == 'down') && yLock == direct) {
	// 		$(this).button('toggle');
	// 		stop(direct);
	// 		yLock = '';
	// 	}
	// });

	$('body').swipeleft(function() {
		if (lock == '') {
			runNeck('left');
			lock = 'x';
		}
	}).swiperight(function() {
		if (lock == '') {
			runNeck('right');
			lock = 'x';
		}
	}).touchend(function() {
		if (lock != '') {
			stopNeck(lock);
			lock = '';
		}
	});
});