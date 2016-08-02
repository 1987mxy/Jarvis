/**
 * 
 */
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
