# CHROME GAMES RANKING SERVER
Google Hackpair에 출품작인 Chrome Games Raning Server 소스입니다. 

# HOW TO USE
클라이언트에서는 직접 URL을 사용하거나 static/ranking.js파일을 include 하여 'ranker' object를 사용하면 됩니다. 요청/응답의 모든 데이터 타입은 json타입으로 사용합니다. API테스트는 [콘솔페이지](http://goo.gl/WDZJt)에서 할 수 있습니다.

## 사용자의 새로운 기록을 추가할 때
### USING API WITH URL
#### URL
```POST http://cg-ranking.appspot.com/user/```
#### PARAMS:
```
{
	ranker:{
		game_name:[w+], 
		user_name:[w+], 
		score:[0-9]
	}
}
```
#### RESPONSE
```
{
	game_name:[w+], 
	user_name:[w+], 
	score:[0-9], 
	rank[0-9] // 현재 점수에 해당하는 랭킹
}
```
### USING LIBRARY
``` javascript
ranking.add(game_name, user_name, score, function(success, data) {
	data = JSON.parse(data)
	var ret = (success) ? ['rank:', data.rank, data.game_name, data.user_name, data.score].join(' ') : 'ERROR';
	console.log(ret);
});
```
