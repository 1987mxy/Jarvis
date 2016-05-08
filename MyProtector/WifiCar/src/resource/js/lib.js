/**
 * 
 */
function run(direct) {
	// $('#test').append('[run ' + direct + ']');
	// return;
	$.get(rudderControlUrl + direct);
}
function stop(axis) {
	console.log('[stop ' + axis + ']')
	return;
	// $.get(rudderControlUrl + axis + 'Stop');
}