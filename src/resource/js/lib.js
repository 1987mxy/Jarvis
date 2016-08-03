/**
 * 
 */

//Neck
var xNeckLock = '',
	yNeckLock = '',
	neckPrefix = 'neck-';
function neckKeyDown (direct) {
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
}
function neckKeyUp (direct) {
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
}
function runNeck(direct) {
//	console.log('[run ' + direct + ']');
//	return;
	$.get(neckCtrlUrl + direct);
}
function stopNeck(axis) {
//	console.log('[stop ' + axis + ']');
//	return;
	$.get(neckCtrlUrl + axis + 'Stop');
}


//Foot
var footLock = '',
	footPrefix = 'foot-';
function footDown (direct) {
	if ((direct == 'front' ||
			direct == 'rear' ||
			direct == 'left' ||
			direct == 'right') && footLock == '') {
		footLock = footPrefix + direct;
		runFoot(direct);
		return true;
	}
	return false;
}
function footUp (direct) {
	if (footLock == footPrefix + direct) {
		stopFoot();
		footLock = '';
		return true;
	}
	return false;
}
function runFoot(direct) {
//	console.log('[run ' + direct + ']');
//	return;
	$.get(footCtrlUrl + direct);
}
function stopFoot() {
//	console.log('[stop ' + axis + ']');
//	return;
	$.get(footCtrlUrl + 'stop');
}

function getLightStatus() {
	$.get(lightCtrlUrl + 'status', function (switchListStatusBit, status) {
		if (status == 'success') {
			$('.light-btn').each(function(){
				var switchNo = $(this).data('light-no'),
				switchBit = Math.pow(2, switchNo - 1),
				switchStatus = (switchBit & switchListStatusBit) == switchBit;
				switchStatus && $(this).addClass('on');
			});
		} else {
			$('.light-btn').addClass('disable');
		}
	});
}

function ctrlLight(switchNo, status, callback) {
	$.get(lightCtrlUrl + 'singlePower' + status + '/' + switchNo, function (resp, status) {
		status == 'success' && $.isFunction(callback) && callback();
	});
}
