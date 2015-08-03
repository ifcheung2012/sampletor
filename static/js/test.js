$(document).ready(function() {
	$("#datagrid1 tr").hover(function() {
		$(this)
			.children("td")
			.addClass("hover");
	}, function() {
		$(this)
			.children("td")
			.removeClass("hover");
	});
	$('#datagrid1 tr:odd').addClass('odd');
	$('#datagrid1 tr:even').addClass('even');

	$('input[name=addtr]').click(function() {
		$('#datagrid1 tr:gt(0):eq(1)').remove();
	});
});