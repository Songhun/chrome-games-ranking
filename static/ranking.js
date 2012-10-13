var ranking = {
	_baseurl: 'http://cg-ranking.appspot.com',
	request: function(method, type, data, cb) {
		$.ajax({
			type: type,
		  url:method,
		  data:data,
			success: function(data) {cb(true, data)},
			error: function(xhr) {cb(false, xhr)},
		});
	},

	add: function(game_name, user_name, score, cb) {
		var data = {'ranker':JSON.stringify({
			game_name:game_name, 
		  user_name:user_name, 
		  score:score
		})};

		this.request(this._baseurl + '/user/', 'post', data, cb);
	},
	top: function(game_name, max, cb) {
		$.ajax({
			type: 'get',
		  url: this._baseurl + '/top/' + game_name + '/' + max,
			success: function(data) {cb(true, data)},
			error: function(xhr) {cb(false, xhr)},
		});
	}
}