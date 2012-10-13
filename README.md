# CHROME GAMES RANKING SERVER
Google Hackpair에 출품작인 Chrome Games Raning Server 소스입니다. 

# HOW TO USE
클라이언트는 static/ranking.js파일을 include 하여 사용하면 됩니다. 요청/응답의 모든 데이터 타입은 json타입으로 사용합니다. static/console.html을 참고하면 사용법을 알 수 있습니다.

##
## 사용자의 새로운 기록을 추가할 때
```
ranking.add(game_name, user_name, score, function(success, data) {
	data = JSON.parse(data)
	var ret = (success) ? ['rank:', data.rank, data.game_name, data.user_name, data.score].join(' ') : 'ERROR';
	console.log(ret);
});
```
