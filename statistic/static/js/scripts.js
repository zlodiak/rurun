$(function() {
	$("#datepickerBegin, #datepickerEnd").datepicker({
		dateFormat: "yy-mm-dd",
		firstDay: 1
	});
});

function getStatistic(unixDatesObj) {


    // http://127.0.0.1:8000/days/1497104260/1497968260
};

function getUnixDatesObj() {
	//console.log('getUnixDatesObj');

	var dateBegin = $('#datepickerBegin').val(), 
		dateEnd = $('#datepickerEnd').val();

	if(!dateBegin || !dateEnd) {
		alert('Необходимо выбрать диапазон дат');
		return;
	}

	var yearBegin = dateBegin.split('-')[0],
		monthBegin = +dateBegin.split('-')[1] - 1,
		dayBegin = dateBegin.split('-')[2]

	if(monthBegin < 10)  { monthBegin = '0' + monthBegin }

	var yearEnd = dateEnd.split('-')[0],
		monthEnd = +dateEnd.split('-')[1] - 1,
		dayEnd = dateEnd.split('-')[2]
		
	if(monthEnd < 10)  { monthEnd = '0' + monthEnd }

	// преобразуем в js-формат
	var dateBeginObj = new Date(yearBegin, monthBegin, dayBegin);
	var dateEndObj = new Date(yearEnd, monthEnd, dayEnd);

	// преобразуем в unix-формат
	var dateBeginUnix = dateBeginObj.getTime() / 1000;
	var dateEndUnix = dateEndObj.getTime() / 1000;

	return {
		'dateBeginUnix': dateBeginUnix,
		'dateEndUnix': dateEndUnix
	}
};

function constructTable(statistic) {
	var tableBodyElem;

	statistic.forEach(function(item) {
		if(item) {
			tableBodyElem += '<tr>'; 
			tableBodyElem += '<td>' + item.fields.created_date.split('T')[0] + '</td>'; 
			tableBodyElem += '<td>' + item.fields.training_time_min + '</td>'; 
			tableBodyElem += '<td>' + item.fields.pulse_avg_bpm + '</td>'; 
			tableBodyElem += '<td>' + item.fields.pulse_max_bpm + '</td>'; 
			tableBodyElem += '</tr>'; 
		}
	});

	var tableElem = '<table class="statistic-table" border="1" celpadding="8"> \
						<thead>\
							<tr>\
								<td>Дата</td>\
								<td>Время тренировки</td>\
								<td>Сердний пульс</td>\
								<td>Максимальный пульс</td>\
							</tr>\
						</thead>\
						<tbody>\
							<tr id=tableBody>' + tableBodyElem + '</tr>\
						</tbody>\
					</table>';

	return tableElem;
};

function displayStatistic() {
	var	unixDatesObj = getUnixDatesObj();
	var statistic, 
		dateBeginUnix = unixDatesObj.dateBeginUnix,
		dateEndUnix = unixDatesObj.dateEndUnix;

    $.ajax({url: "http://127.0.0.1:8000/days/" + dateBeginUnix + "/" + dateEndUnix, success: function(result){
		statistic = JSON.parse(result);	
		console.log(123);
		alert(statistic);
		var table = constructTable(statistic);
		$('#statisticTableWrap').append(table);
		
    }});
};