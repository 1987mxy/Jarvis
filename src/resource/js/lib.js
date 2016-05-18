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
	$.get(neckCtrlUrl + direct);
}
function stopFoot(axis) {
//	console.log('[stop ' + axis + ']');
//	return;
	 $.get(neckCtrlUrl + axis + 'Stop');
}

function getLightStatus() {
	$.get(lightCtrlUrl + 'status', function(switchListStatusBit){
		$('.light-switch').each(function(){
			var switchNo = $(this).data('switch-no'),
				switchBit = Math.pow(2, switchNo - 1),
				switchStatus = (switchBit & switchListStatusBit) == switchBit;
			console.log('setState',switchStatus);
//			$(switchSelector).bootstrapSwitch('state', switchStatus);
			$(this).bootstrapSwitch({
				state: switchStatus,
				onSwitchChange: function (e, isOpen) {
					ctrlLight(switchNo, isOpen);
				}
			});
		});
	});
}

function ctrlLight(switchNo, isOpen) {
	$.get(lightCtrlUrl + 'singlePower' + (isOpen ? 'On' : 'Off') + '/' + switchNo);
}
