/**
 * 
 */
$(function() {
	getLightStatus();
	
	$('.light-btn').click(function(){
		var _thisStatus = '',
			$this = $(this);
		if (!$this.hasClass('disable')) {
			if ($this.hasClass('on')) {
				_thisStatus = 'Off';
			} else {
				_thisStatus = 'On';
			}
		}
		_thisStatus && ctrlLight($this.data('light-no'), _thisStatus, function () {
			$this.toggleClass('on');
		});
	});
});