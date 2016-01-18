//Allow slider dragging on mobile devices
$('#widget').draggable()

//Responsive button press -->
$('.btn-left').click(function() {
		$(this).attr('class', 'btn btn-default btn-left active');
		right_button = '.btn-right#'.concat(this.id)
		$(right_button).attr('class', 'btn btn-default btn-right');
	});
$('.btn-right').click(function() {
		$(this).attr('class', 'btn btn-default btn-right active');
		left_button = '.btn-left#'.concat(this.id)
		$(left_button).attr('class', 'btn btn-default btn-left');
	});