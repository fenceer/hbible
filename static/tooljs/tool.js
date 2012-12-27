$('.method').click(function() {
	var method = $(this).html();
	var args = $(this).next().html();
	var url = $(this).attr('href');
	args = args.replace('(', '').replace(')', '').split(',');
	if (args.length == 1) {
		if (args[0] == '') {
			args = [];
		}
	}

	form = createForm(args, url, method);
	$('#form .J-api-form').remove();
	$('#form').append(form);

	form.find('.submit').click(submit);

	return false;
});

$('#controller').change(function() {
	var ctrl = $(this).val();
	if (ctrl == 'All') {
		window.location.replace('/apidoc');
	} else {
		window.location.replace('/apidoc/' + ctrl);
	}
});

function submit() {
	var method = $(this).attr('method');
	var url = $.trim($('#J-url-field input').val());
	var isopen = $(this).attr('open');
	viewResult('');

	var query;
	if (method == 'get') {
		if (isopen == 'open') {
			query = buildQuery('string');
			window.open(url + query);
		} else {
			query = buildQuery('object');
			viewPost(query, url, method);
			$.get(url, query, function(data) {
				viewResult(data);
			}, 'text');
		}

	}
	if (method == 'post') {
		query = buildQuery('object');
		viewPost(query, url, method);
		$.post(url, query, function(data) {
			viewResult(data);
		}, 'text');
	}
	return false;
}

function viewResult(data) {
	$('#J-result-view').html(data);
}

function viewPost(data, url, method) {
	$('#J-post-view').html(JSON.stringify(data));
	$('#J-url-view').html(url);
	$('#J-method-view').html(method);
}

function buildQuery(type) {
	var query = '';
	if (type == 'string') {
		$('#form li').each(function() {
			if (!$(this).is('#J-url-field')) {
				var p = $(this).find('label').html();
				var v = $.trim($(this).find('input').val());
				if (v != '') {
					query += '&' + p + '=' + encodeURIComponent(v);
				}
			}
		});
		if (query != '') {
			return query.replace(/^&/, '?');
		}
	}
	if (type == 'object') {
		query = {};
		$('#form li').each(function() {
			if (!$(this).is('#J-url-field')) {
				var p = $(this).find('label').html();
				var v = $.trim($(this).find('input').val());
				if (v != '') {
					query[p] = v;
				}
			}
		});
	}
	return query;
}

function createForm(args, url, method) {
	var div = $('<div/>', {
		'class' : 'api-item-form clearfix J-api-form'
	});
	var ul = $('<ul/>');
	ul.append(createUrlField(url));
	for (var i = 0; i < args.length; i++) {
		var arg = args[i];
		var field;
		if (arg.substring(0, 1) == '#') {
			field = createField(arg.replace('#', ''), false);
		} else {
			field = createField(arg, true);
		}
		ul.append(field);
	}
	var btns = $('<div/>', {
		'class' : 'btns'
	});
	var submit = $('<a/>', {
		href : url,
		'class' : 'submit'
	}).html('AJAX');
	div.append(ul);
	if (method == 'GET') {
		submit.attr('method', 'get');
		var open = submit.clone().attr('open', 'open').html('打开');
		btns.append(open);
	}
	if (method == 'POST') {
		submit.attr('method', 'post');
	}
	btns.append(submit);
	div.append(btns);
	return div;
}

function createUrlField(url) {
	var li = $('<li></li>', {
		'class' : 'url-field',
		'id' : 'J-url-field'
	});
	var label = $('<label/>').html('URL');
	var input = $('<input/>', {
		type : 'text',
		'class' : 'tinp',
		value : url
	})
	return li.append(label).append(input);
}

function createField(arg, ismust) {
	var li = $('<li></li>');
	var label = $('<label/>').html(arg);
	if (ismust) {
		label.addClass('must');
	}
	var input = $('<input/>', {
		type : 'text',
		'class' : 'tinp'
	})
	return li.append(label).append(input);
}