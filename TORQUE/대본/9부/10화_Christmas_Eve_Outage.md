# TORQUE — 9부 10화

## Christmas Eve Outage (성탄 전야의 장애)

> **표기 전용 정보 (낭독하지 않음)**
> - 부/화: 9부 10화 · 서사 기능: 현장 위기, Lily의 첫 실전 기여, 고객과의 신뢰 확인
> - 배경: Sam의 집 부엌(새벽 2시 40분) → I-70 동쪽, Sam의 트럭(새벽 3시 반) → Helix Cloud 리킹 카운티 단지 3동 펌프실·제어실(새벽 4시~7시) → 3동 옥상 냉각기 앞(동틀 무렵) → 귀갓길 트럭(아침). 2026년 12월 24일 목요일 크리스마스이브, 북극 한파, 영하 22도.
> - 등장인물: Sam, Lily, Erin(전화), Marcus Webb, Tess Morrow, Brandon, Wen(전화), Raj Mehta(전화), Kayla(문자)
> - 실제 사건 / 현안 태그: 겨울 한파와 전력·냉각 설비, 데이터센터 이중화(failover)와 가동률, 센서 고장과 제어 충돌, 현장 비상 절차(MOP)
> - 난이도: B2 · 턴 수: 150
> - 이번 화의 핵심 표현: "outage", "failover", "on call", "under pressure", "save the day", "fault code", "hunting", "root cause"
> - 복선/연결: 8부 4화 Tess·Brandon·펌웨어 5.5 · Lily의 코업 지원(→12부 11화) · 국방 법안의 'study' 조항 삭제(9부 7화) · 위원회 보좌관의 연락(→9부 11화)

---

## 대본

001. LILY: Dad, why are you wearing your boots in the kitchen at two forty in the morning?
    릴리: 아빠, 새벽 두 시 사십 분에 왜 부엌에서 장화를 신고 있어?

002. SAM: Go back to bed, Lil, because it's just work.
    샘: 다시 자, 릴. 그냥 일이야.

003. LILY: But it's Christmas Eve, Dad.
    릴리: 근데 크리스마스이브잖아, 아빠.

004. SAM: It's Christmas Eve, and it's minus seven outside, and one of Raj's buildings is having a very bad night. Marcus is already on his way. I'm going to meet him there.
    샘: 크리스마스이브고, 밖은 영하 22도고, 라지네 건물 하나가 아주 안 좋은 밤을 보내고 있어. 마커스는 벌써 가는 중이야. 거기서 만나기로 했어.

005. LILY: What's wrong with the building? Is something on fire?
    릴리: 건물에 뭐가 문젠데? 뭐 불이라도 났어?

006. SAM: The cooling pumps in building three keep stopping and starting every ninety seconds, and they're our pumps. Tess called me herself, which she never does.
    샘: 3동 냉각 펌프가 90초마다 계속 멈췄다 돌았다 하는데, 우리 펌프야. 테스가 직접 전화했어. 그 사람 절대 그런 적 없는데.

007. LILY: Every ninety seconds, exactly?
    릴리: 90초마다, 정확히?

008. SAM: That's what she said, but why do you ask?
    샘: 그렇게 말했어. 근데 왜 물어?

009. LILY: Because exact numbers are weird, since broken things are usually messy. Can I come with you?
    릴리: 정확한 숫자는 이상하니까. 고장 난 건 보통 지저분하거든. 나 같이 가도 돼?

010. SAM: No. It's an hour away and it's a data center at three a.m. You'll be bored and cold.
    샘: 안 돼. 한 시간 거리에, 새벽 세 시 데이터센터야. 지루하고 추울 거야.

011. LILY: Dad, I'm coming, because you need somebody who can read logs. Marcus is great, but he's one person, and you read logs like Grandpa reads text messages.
    릴리: 아빠, 나 갈 거야. 로그 읽을 줄 아는 사람이 필요하잖아. 마커스 아저씨 대단하지만 혼자고, 아빠는 할아버지가 문자 읽듯이 로그를 읽잖아.

012. SAM: That's not fair, because I read logs just fine with my glasses.
    샘: 그건 너무하다. 나 안경 쓰면 로그 잘 읽어.

013. LILY: You held your phone at arm's length last week and said "What's this little picture?"
    릴리: 지난주에 폰을 팔 길이만큼 멀리 들고 "이 작은 그림은 뭐야?" 했잖아.

014. SAM: It was a very small picture.
    샘: 아주 작은 그림이었어.

015. LILY: It was an emoji. Give me two minutes, and I'll wear two coats.
    릴리: 이모지였어. 2분만 줘, 코트 두 벌 입을게.

016. SAM: Your mother's going to kill me, and on Christmas Eve, no less.
    샘: 너희 엄마가 날 죽일 거야. 그것도 크리스마스이브에.

017. LILY: Mom's working the night shift at the ER, so I'll text her, and she'll say yes.
    릴리: 엄마는 응급실 야간 근무 중이니까 문자할게. 된다고 할 거야.

018. SAM: And how do you know that?
    샘: 그걸 어떻게 알아?

019. LILY: Because I'll tell her you said I could.
    릴리: 아빠가 된다고 했다고 할 거니까.

020. ERIN: I got Lily's text, so where are you two right now?
    에린: 릴리 문자 받았어. 둘 지금 어디야?

021. SAM: I-70, past Columbus. Lily's asleep in the passenger seat with a laptop on her knees. She was asleep before we hit the highway.
    샘: I-70, 콜럼버스 지났어. 릴리는 조수석에서 무릎에 노트북 올리고 자. 고속도로 타기도 전에 잠들었어.

022. ERIN: So she came for the nap.
    에린: 그러니까 낮잠 자러 따라간 거네.

023. SAM: She came because she knew I'd say no. How's the ER tonight?
    샘: 내가 안 된다고 할 줄 알아서 따라온 거지. 오늘 밤 응급실은 어때?

024. ERIN: It's frozen pipes, frozen fingers, and a man who tried to start his car with a hair dryer, same as every winter. Sam, the roads are ice, so drive like I'm in the car.
    에린: 언 수도관, 언 손가락, 헤어드라이어로 차 시동 걸려던 아저씨까지, 겨울마다 똑같아. 샘, 길이 빙판이니까 내가 차에 타고 있는 것처럼 운전해.

025. SAM: I am, at forty-five miles an hour, and a truck just passed me.
    샘: 그러고 있어, 시속 45마일로. 트럭이 방금 날 추월했어.

026. ERIN: Let it pass. So what's happening at Helix, and is it bad?
    에린: 추월하라고 해. 그래서 헬릭스는 어떻게 된 거야? 심각해?

027. SAM: Building three's cooling is going in and out. Their systems switched part of the hall over to the backup pumps. That's called failover. It's working, but the backups are old and slower.
    샘: 3동 냉각이 들어왔다 나갔다 해. 시스템이 홀 일부를 예비 펌프로 넘겼어. 그걸 페일오버라고 해. 작동은 하는데 예비 펌프가 낡아서 느려.

028. ERIN: So it's like when my ER loses power and the generator kicks in.
    에린: 그러니까 우리 응급실 전기 나가서 발전기 돌아가는 거랑 비슷하네.

029. SAM: Exactly like that. Except the generator is tired, and the patients are computers that cost forty thousand dollars each.
    샘: 딱 그거야. 다만 발전기가 지쳐 있고, 환자가 한 대에 4만 달러짜리 컴퓨터라는 것만 빼면.

030. ERIN: Are the patients dying? Tell me in my language.
    에린: 환자들 죽어 가? 내 말로 해 봐.

031. SAM: Not yet, because Raj says they're slowing the computers down so they make less heat, which buys time. If the backups can't keep up, they shut down part of the hall, and that's an outage.
    샘: 아직은. 라지 말로는 열을 덜 내게 컴퓨터 속도를 늦춰서 시간을 벌고 있대. 예비 펌프가 못 따라가면 홀 일부를 끄는데, 그게 장애야.

032. ERIN: How long do you have?
    에린: 시간이 얼마나 있어?

033. SAM: Raj said, "Before the West Coast wakes up." So about four hours.
    샘: 라지가 "서부 해안이 일어나기 전까지"래. 그러니까 네 시간쯤.

034. ERIN: Okay, and you know exactly what I'm going to say, don't you?
    에린: 좋아. 내가 무슨 말 할지 정확히 알지?

035. SAM: "I triage for a living, Sam."
    샘: "난 사람 우선순위 정하는 게 직업이야, 샘."

036. ERIN: No, I was going to say, "Bring my daughter home in time for dinner" at seven o'clock, because my mother's coming, and she's bringing the green bean thing.
    에린: 아니, "일곱 시 저녁 시간에 맞춰 내 딸 데려와"라고 하려고 했어. 우리 엄마 오시는데, 그 껍질콩 요리 가져오신대.

037. SAM: The green bean thing at seven o'clock, I promise.
    샘: 일곱 시에 그 껍질콩 요리, 약속해.

038. LILY: Did somebody say green beans?
    릴리: 누가 껍질콩이라고 했어?

039. SAM: Your mom, so go back to sleep, because we've got twenty minutes left.
    샘: 너희 엄마가. 다시 자, 20분 남았어.

040. LILY: I'm awake, and I'm reading the alarm history Marcus sent. Dad, something's weird about these times.
    릴리: 깼어. 마커스 아저씨가 보낸 경보 기록 읽고 있어. 아빠, 이 시간들 뭔가 이상해.

041. TESS: Sam, thank God you're here, so badge in and follow me. Is that your daughter?
    테스: 샘, 와 줘서 다행이에요. 배지 찍고 따라와요. 그 애가 따님이에요?

042. SAM: This is Lily, a mechanical engineering student who's here to read logs, and I'll take responsibility for her.
    샘: 릴리예요. 로그 읽으러 온 기계공학과 학생이고, 제가 책임질게요.

043. TESS: She gets a visitor badge and safety glasses, and she doesn't touch anything with a red tag, ever. Lily, that's my one rule, so can you live with that?
    테스: 방문자 배지랑 보안경 쓰고, 빨간 태그 붙은 건 절대 아무것도 만지지 않기. 릴리, 그게 내 유일한 규칙인데 지킬 수 있어요?

044. LILY: Yes, ma'am, I won't touch anything red.
    릴리: 네, 빨간 건 아무것도 안 만질게요.

045. TESS: Good. Brandon's in the pump room with Marcus, and they've been here since two.
    테스: 좋아요. 브랜던이 마커스랑 펌프실에 있는데, 두 시부터 있었어요.

046. BRANDON: Mr. Kowalski, merry Christmas, I guess. It's your lock, your key, your life, so everything we've touched is tagged.
    브랜던: 코월스키 사장님, 메리 크리스마스, 겠죠. 내 자물쇠, 내 열쇠, 내 목숨이니까, 저희가 만진 건 전부 태그 붙였어요.

047. SAM: Good man. Marcus, what have we got so far?
    샘: 잘했어. 마커스, 지금까지 상황이 어때?

048. MARCUS: Pumps P-3-1 through P-3-8. All Ferrox. Every ninety seconds, they ramp up to full speed, the current spikes, our firmware sees the current go over the limit, and it backs them off. Then the building tells them to go full speed again.
    마커스: P-3-1부터 P-3-8까지 펌프. 전부 페록스 거예요. 90초마다 최고 속도로 올라가면 전류가 튀고, 우리 펌웨어가 전류 한계 초과를 보고 속도를 줄여요. 그러면 건물이 다시 최고 속도로 돌라고 명령하고요.

049. SAM: So the building and our firmware are fighting each other.
    샘: 그러니까 건물이랑 우리 펌웨어가 서로 싸우고 있는 거네.

050. MARCUS: They're fighting each other, which engineers call hunting, where two controllers chase each other around a number and neither one ever wins.
    마커스: 서로 싸우고 있어요. 엔지니어들은 그걸 헌팅이라고 하는데, 제어기 두 개가 어떤 숫자 주위를 서로 쫓아다니면서 어느 쪽도 못 이기는 거예요.

051. TESS: And every time the pumps back off, the flow drops, the hall gets warmer, and my system fails over to the old pumps. Then it tries to switch back. My alarm screen looks like a Christmas tree.
    테스: 그리고 펌프가 속도를 줄일 때마다 유량이 떨어지고, 홀이 더워지고, 우리 시스템이 낡은 펌프로 넘어가요. 그러다 다시 돌아오려 하고요. 제 경보 화면이 크리스마스트리 같아요.

052. LILY: Why does the building want full speed, when it's minus seven outside? You'd think you need less cooling, not more.
    릴리: 밖이 영하 22도인데 건물은 왜 최고 속도를 원해요? 냉각이 더 필요한 게 아니라 덜 필요할 것 같은데요.

053. TESS: Good question. In this kind of cold, the glycol in the outdoor loop can freeze if it moves too slowly. So when it gets very cold outside, the building goes into freeze protection. Full speed, to keep things moving.
    테스: 좋은 질문이에요. 이렇게 추우면 실외 순환 회로의 글리콜이 너무 천천히 움직일 때 얼 수 있어요. 그래서 밖이 아주 추워지면 건물이 동결 방지 모드로 들어가요. 계속 흐르게 최고 속도로요.

054. SAM: In plain English, Lil, glycol is antifreeze. Like in a car. It runs through pipes on the roof, gives the heat to the cold air, and comes back down cold.
    샘: 쉽게 말하면, 릴, 글리콜은 부동액이야. 자동차에 넣는 거. 옥상 배관을 돌면서 열을 찬 공기에 주고 차가워져서 다시 내려와.

055. LILY: I know what glycol is, Dad.
    릴리: 글리콜이 뭔지는 알아, 아빠.

056. SAM: I was explaining it for Brandon.
    샘: 브랜던 들으라고 설명한 거야.

057. BRANDON: I also know what glycol is, sir.
    브랜던: 저도 글리콜이 뭔지 알아요, 사장님.

058. MARCUS: Here's the problem on our side. Cold glycol is thick like syrup, so at this temperature it takes much more current to push it, and our current limit was set for normal winters, because we never tested at minus seven on Betsy.
    마커스: 우리 쪽 문제는 이거예요. 차가운 글리콜은 시럽처럼 걸쭉해서 이 온도에선 밀어내는 데 전류가 훨씬 많이 들어요. 근데 우리 전류 한계는 보통 겨울에 맞춰져 있었어요. 베치에서 이 온도로는 시험해 본 적이 없거든요.

059. SAM: That's on us, because we should have tested colder.
    샘: 그건 우리 책임이네. 더 추운 조건으로 시험했어야 했어.

060. MARCUS: That's partly on us. I can raise the cold-weather current limit, which is a setting and not new code, and that should stop the fighting.
    마커스: 일부는 우리 책임이에요. 한랭 시 전류 한계를 올릴 수 있는데, 새 코드가 아니라 설정값이에요. 그러면 싸움이 멈출 거예요.

061. TESS: Not in my building, not without the MOP, the method of procedure, with written steps that are reviewed and approved. I don't care if it's one number, because I've seen one number take down a hall.
    테스: 제 건물에선 MOP 없이는 안 돼요. 작업 절차서요. 단계를 적고, 검토하고, 승인받아야 해요. 숫자 하나라도 상관없어요. 숫자 하나가 홀 하나를 날리는 걸 봤거든요.

062. SAM: She's right, Marcus, so write the MOP.
    샘: 테스 말이 맞아, 마커스. 절차서 써.

063. MARCUS: I'm writing it now, and it'll take forty minutes with Raj's approval.
    마커스: 지금 쓰고 있어요. 라지 승인까지 40분 걸릴 거예요.

064. TESS: Raj is driving in from Granville. He'll approve from the car. Brandon, call him, and make him pull over to read it.
    테스: 라지는 그랜빌에서 차 몰고 오는 중이에요. 차에서 승인할 거예요. 브랜던, 전화해서 차 세우고 읽으라고 해.

065. BRANDON: He won't pull over, because he never pulls over for anything.
    브랜던: 안 세우실 거예요. 무슨 일이 있어도 차는 안 세우시거든요.

066. TESS: Then tell him I said so.
    테스: 그럼 내가 그러라고 했다고 해.

067. LILY: Can I see the trend screen, the one with the temperatures?
    릴리: 추이 화면 볼 수 있어요? 온도 나오는 거요.

068. TESS: You can look all you want, just don't touch the mouse.
    테스: 얼마든지 봐도 되는데, 마우스만 만지지 마요.

069. LILY: I won't. Brandon, which line is the outdoor temperature?
    릴리: 안 만질게요. 브랜던, 어느 선이 바깥 온도예요?

070. BRANDON: The blue one, which comes from the sensor on the roof, by the dry coolers.
    브랜던: 파란 거요. 옥상 건식 냉각기 옆에 있는 센서에서 와요.

071. LILY: It says minus forty, though.
    릴리: 근데 영하 40도라고 나와요.

072. BRANDON: Yeah, it's cold, because it's really, really cold out there.
    브랜던: 네, 춥잖아요. 밖에 진짜 진짜 추워요.

073. LILY: It's cold, but it's not minus forty, because the weather app says minus seven Fahrenheit. And the line isn't moving, it's been perfectly flat since one fifty-one a.m.
    릴리: 춥긴 한데 영하 40도는 아니에요. 날씨 앱은 화씨 영하 7도래요. 그리고 선이 안 움직여요. 새벽 1시 51분부터 완전히 평평해요.

074. TESS: Let me see that for a second.
    테스: 그거 잠깐 나 좀 보자.

075. LILY: And the hunting started at one fifty-two, just one minute later.
    릴리: 그리고 헌팅은 딱 1분 뒤인 1시 52분에 시작됐어요.

076. SAM: Lil, slow down, and tell me what you're saying.
    샘: 릴, 천천히. 무슨 말인지 말해 봐.

077. LILY: Minus forty is a weird number, Dad. It's the one temperature where Celsius and Fahrenheit are the same. My physics professor told us that. He also said a lot of cheap sensors use it as a default.
    릴리: 영하 40은 이상한 숫자야, 아빠. 섭씨랑 화씨가 똑같아지는 유일한 온도야. 물리 교수님이 말해 줬어. 싼 센서들이 그걸 기본값으로 많이 쓴다는 말도 했고.

078. MARCUS: And what do you mean by a default?
    마커스: 기본값이라는 게 무슨 뜻이에요?

079. LILY: Meaning when the sensor breaks, or loses power, it doesn't say "I'm broken." It says "minus forty." That's its fault code. It's the lowest number it can say.
    릴리: 센서가 고장 나거나 전원을 잃으면 "나 고장 났어"라고 말하지 않고 "영하 40"이라고 말한다는 뜻이에요. 그게 고장 코드예요. 그 센서가 말할 수 있는 제일 낮은 숫자고요.

080. TESS: Brandon, what model is that roof sensor?
    테스: 브랜던, 그 옥상 센서 모델이 뭐야?

081. BRANDON: I'll check the drawings, and it's, uh… yeah, it's right in the manual: "On sensor failure, output defaults to minus forty degrees."
    브랜던: 도면 확인해 볼게요. 그게, 어… 네, 설명서에 바로 있어요. "센서 고장 시 출력은 영하 40도로 기본 설정된다."

082. TESS: Oh, you have got to be kidding me.
    테스: 아, 말도 안 돼.

083. SAM: So the sensor died at one fifty-one.
    샘: 그러니까 센서가 1시 51분에 죽었다는 거네.

084. LILY: Probably froze, or the wire cracked in the cold. And at one fifty-two, the building saw minus forty, believed it, and went into the strongest freeze protection mode. Full speed, all pumps.
    릴리: 아마 얼었거나 추위에 전선이 갈라졌을 거야. 그리고 1시 52분에 건물이 영하 40을 보고, 그걸 믿고, 가장 강한 동결 방지 모드로 들어간 거지. 최고 속도, 펌프 전부.

085. MARCUS: And at the real temperature the glycol was already thick, so full speed meant huge current, and our firmware backed off, and then the building pushed again, every ninety seconds.
    마커스: 그리고 실제 온도에서도 글리콜이 이미 걸쭉해서 최고 속도는 엄청난 전류를 뜻했고, 우리 펌웨어가 물러나면 건물이 다시 밀어붙인 거예요. 90초마다요.

086. LILY: Ninety seconds is the building's retry timer, which is in the settings, because I saw it in the export Marcus sent.
    릴리: 90초는 건물의 재시도 타이머예요. 설정에 있는데, 마커스 아저씨가 보낸 내보내기 파일에서 봤어요.

087. TESS: So exact numbers really are weird.
    테스: 그러니까 정확한 숫자는 정말 이상하네.

088. LILY: That's what I said in the kitchen!
    릴리: 내가 부엌에서 한 말이 그거예요!

089. SAM: She did. At two forty a.m. I told her to go back to bed.
    샘: 했어요. 새벽 두 시 사십 분에. 난 다시 자라고 했고요.

090. TESS: So the root cause isn't your pump, it's my sensor.
    테스: 그러니까 근본 원인은 당신네 펌프가 아니라 우리 센서네요.

091. MARCUS: The root cause is your sensor. But our current limit made it worse. If our pumps had been able to just run, there would've been no fight.
    마커스: 근본 원인은 그쪽 센서예요. 근데 우리 전류 한계가 상황을 더 나쁘게 만들었어요. 우리 펌프가 그냥 돌 수만 있었으면 싸움은 없었을 거예요.

092. SAM: So it's both of us, okay, and what's the fix?
    샘: 그러니까 둘 다네, 좋아. 해결책은?

093. TESS: There are two parts. First, I tell the building to stop believing the roof sensor and use the return glycol temperature instead, because that's a real number. Brandon, write it into Marcus's MOP, in the same document.
    테스: 두 단계예요. 첫째, 건물이 옥상 센서를 믿지 말고 대신 글리콜 환수 온도를 쓰게 할게요, 그건 진짜 숫자니까. 브랜던, 마커스의 절차서에 같은 문서로 넣어.

094. MARCUS: Second, I raise our cold-weather current limit, with a ramp, so the pumps speed up slowly instead of all at once.
    마커스: 둘째, 우리 한랭 시 전류 한계를 올려요. 램프를 둬서 펌프가 한 번에 말고 천천히 속도를 올리게요.

095. TESS: One document, two changes, one approval, and Raj will love that, because he loves short emails.
    테스: 문서 하나, 변경 두 개, 승인 하나. 라지가 좋아할 거예요, 짧은 메일 좋아하거든요.

096. LILY: Can I say one more thing before you send it?
    릴리: 보내기 전에 하나만 더 말해도 돼요?

097. TESS: You've earned one more thing, so go ahead, Lily.
    테스: 하나 더 말할 자격 있어요. 해 봐요, 릴리.

098. LILY: The roof sensor is still broken. Even after this, if somebody switches the building back to it next week, the same thing happens again. Somebody should go up and look at it.
    릴리: 옥상 센서는 아직 고장 나 있어요. 이거 하고 나서도 다음 주에 누가 건물을 다시 그 센서로 바꾸면 똑같은 일이 또 생겨요. 누가 올라가서 봐야 해요.

099. BRANDON: On the roof? It's minus seven with the wind, so it's like minus thirty up there.
    브랜던: 옥상에요? 바람까지 치면 화씨 영하 7도라서, 거기 올라가면 영하 30도 같을 거예요.

100. SAM: I'll go with you, because I've got two coats too.
    샘: 같이 갈게. 나도 코트 두 벌 있거든.

101. TESS: Nobody goes up until the change is done and the hall is stable, because that's the MOP too. First stop the bleeding. Then fix the wound.
    테스: 변경이 끝나고 홀이 안정될 때까진 아무도 못 올라가요. 그것도 절차거든요. 먼저 피를 멈추고, 그다음에 상처를 고치는 거죠.

102. SAM: My wife says the same thing, almost word for word.
    샘: 우리 아내도 거의 토씨 하나 안 틀리고 똑같이 말해요.

103. TESS: Your wife sounds like a smart woman.
    테스: 아내분이 똑똑한 분인가 봐요.

104. SAM: She's an ER nurse, and she's working a double right now.
    샘: 응급실 간호사인데, 지금 연속 근무 중이에요.

105. MARCUS: The MOP's done, two pages, and I sent it to Raj. Wen's on the phone, because she wants to check my numbers.
    마커스: 절차서 끝났어요, 두 장이고 라지한테 보냈어요. 웬이 전화로 연결돼 있는데, 제 숫자를 확인하고 싶대요.

106. WEN: Marcus, your new limit is fine, but make the ramp eight seconds, not five, because cold glycol needs time. It's like my father, who you can't rush in the morning.
    웬: 마커스, 새 한계는 괜찮은데 램프는 5초 말고 8초로 해요. 차가운 글리콜은 시간이 필요하거든요. 아침에 재촉하면 안 되는 우리 아버지 같아요.

107. MARCUS: Eight seconds, I'm changing it now.
    마커스: 8초, 지금 바꿀게요.

108. WEN: Lily, Marcus told me about the minus forty, and that was very good.
    웬: 릴리, 마커스가 영하 40 얘기 해 줬어요. 아주 잘했어요.

109. LILY: Thanks, Wen, but is it okay that I'm here, when I'm not, like, an employee?
    릴리: 고마워요, 웬. 근데 저 직원도 아닌데 여기 있어도 괜찮은 거예요?

110. WEN: You're not an employee, you're a witness, so write down everything you saw, with times, tonight before dinner, because that's a root cause report.
    웬: 직원은 아니고 증인이죠. 본 걸 전부 시간이랑 같이 오늘 밤 저녁 먹기 전에 적어요. 그게 근본 원인 보고서예요.

111. LILY: Like a homework assignment, over Christmas break?
    릴리: 크리스마스 방학에 숙제처럼요?

112. WEN: Like an interview, because Earl and I will read it.
    웬: 면접처럼요. 얼이랑 제가 읽을 거니까.

113. SAM: Wen.
    샘: 웬.

114. WEN: I'm not saying anything, Sam, and I'm recused from nothing, because you're the one who's recused. Merry Christmas.
    웬: 아무 말도 안 했어요, 샘. 전 빠질 이유가 없어요. 빠진 사람은 당신이죠. 메리 크리스마스.

115. BRANDON: Raj approved it from a gas station in Newark! He says, "Go, and tell Tess I pulled over."
    브랜던: 라지 님이 뉴어크 주유소에서 승인했어요! "진행하세요, 그리고 테스한테 차 세웠다고 전해 줘요"래요.

116. TESS: Okay, everybody quiet for step one. Brandon, switch freeze protection to return glycol temperature, and read it back to me.
    테스: 좋아요, 1단계니까 다들 조용히. 브랜던, 동결 방지를 글리콜 환수 온도 기준으로 바꾸고 복창해.

117. BRANDON: Switching freeze protection input from roof sensor to return glycol in building three, and it's done. Return glycol reads minus four Celsius, and freeze protection is stepping down.
    브랜던: 3동 동결 방지 입력을 옥상 센서에서 글리콜 환수로 전환, 완료. 글리콜 환수 섭씨 영하 4도, 동결 방지 단계 하향 중.

118. TESS: Step two is yours, Marcus.
    테스: 2단계는 네 차례야, 마커스.

119. MARCUS: I'm applying the new cold-weather current limit and the eight-second ramp to P-3-1 through P-3-8, one at a time, and P-3-1 is done and stable.
    마커스: P-3-1부터 P-3-8까지 새 한랭 시 전류 한계와 8초 램프를 하나씩 적용 중. P-3-1 완료, 안정.

120. LILY: The current line just went smooth, so look, there are no more teeth.
    릴리: 전류 그래프가 방금 매끄러워졌어요. 봐요, 톱니가 없어졌어요.

121. MARCUS: P-3-2 and P-3-3 are done, and hold on, P-3-4 through eight are all done, and all of them are stable.
    마커스: P-3-2, P-3-3 완료. 잠깐만, P-3-4부터 8까지 전부 완료, 전부 안정.

122. TESS: Flow is back to normal and hall temperature is dropping, and my system is switching back from the old pumps slowly, like it doesn't trust us yet.
    테스: 유량 정상 복귀, 홀 온도 떨어지는 중이에요. 시스템이 낡은 펌프에서 천천히 돌아오고 있어요, 아직 우릴 못 믿는 것처럼.

123. BRANDON: Ninety seconds with no alarm, and a hundred and eighty with no alarm.
    브랜던: 90초, 경보 없음. 180초, 경보 없음.

124. SAM: Nobody say anything for another ten minutes.
    샘: 10분 더 아무도 아무 말 하지 마.

125. LILY: Okay, but I'm going to be smiling, and you can't stop me from smiling.
    릴리: 알았어, 근데 나 웃고 있을 거야. 웃는 건 못 막아.

126. BRANDON: There's the sensor, so look at the wire, because the cold cracked the jacket right at the connector, and water got in and froze.
    브랜던: 저기 센서 있어요. 전선 좀 보세요. 추위 때문에 커넥터 바로 옆 피복이 갈라져서 물이 들어가 얼었어요.

127. SAM: All this for a five-dollar wire.
    샘: 5달러짜리 전선 하나 때문에 이 난리였네.

128. BRANDON: A five-dollar wire that almost took down a hall. I'll replace it today and put a heat jacket on it. And I'm writing a note in the system: "Never default to the roof."
    브랜던: 홀 하나를 날릴 뻔한 5달러짜리 전선이죠. 오늘 갈고 보온 피복 씌울게요. 그리고 시스템에 메모 남길 거예요. "절대 옥상을 기본으로 하지 말 것."

129. SAM: Look at that sky, because the sun's coming up over the cooling towers.
    샘: 저 하늘 좀 봐. 냉각탑 위로 해가 뜬다.

130. LILY: It's beautiful, and I can't feel my face.
    릴리: 예쁘다. 그리고 얼굴에 감각이 없어.

131. SAM: Lil, about what you did in there, I want you to know something. I didn't see it and Marcus didn't see it, and Tess has worked here for twelve years and didn't see it.
    샘: 릴, 네가 저 안에서 한 거, 이건 알았으면 좋겠어. 나도 마커스도 못 봤고, 테스는 여기서 12년 일했는데도 못 봤어.

132. LILY: They would have found it in another hour, maybe two.
    릴리: 한 시간, 아니면 두 시간만 더 있었으면 찾았을 거야.

133. SAM: Maybe. But you saw it in the truck, half asleep, with a laptop on your knees. "Exact numbers are weird." Where did you learn that?
    샘: 그럴 수도. 근데 넌 트럭에서, 반쯤 자면서, 무릎에 노트북 올리고 봤어. "정확한 숫자는 이상하다." 그거 어디서 배웠어?

134. LILY: From you. When I was ten. A motor on Betsy failed at exactly two thousand RPM, every time, and you said, "When it's exact, it's not the motor. It's something telling the motor what to do."
    릴리: 아빠한테서. 열 살 때. 베치에서 모터 하나가 매번 정확히 2,000RPM에서 고장 났는데, 아빠가 그랬어. "정확할 땐 모터 문제가 아니야. 모터한테 뭘 하라고 시키는 무언가의 문제지."

135. SAM: Wait, I said that?
    샘: 잠깐, 내가 그런 말을 했어?

136. LILY: You said it to Earl, while I was under the workbench eating crackers.
    릴리: 얼 아저씨한테 했어. 난 작업대 밑에서 크래커 먹고 있었고.

137. SAM: Raj is calling, so hang on. Raj, good morning.
    샘: 라지 전화다, 잠깐만. 라지, 좋은 아침이에요.

138. RAJ: Good morning? Sam, it's a great morning, because I just walked into building three and there are no alarms. The AI customer's job never stopped, and they don't even know anything happened, which is the best kind of save.
    라지: 좋은 아침이요? 샘, 끝내주는 아침이에요. 방금 3동 들어왔는데 경보가 하나도 없어요. AI 고객 작업은 한 번도 안 멈췄고 무슨 일이 있었는지도 몰라요. 그게 최고의 구조죠.

139. SAM: The root cause was your roof sensor. But our current limit made it worse. We'll have a fix for every campus by January, and we're going to test at minus thirty on Betsy from now on.
    샘: 근본 원인은 그쪽 옥상 센서였어요. 근데 우리 전류 한계가 상황을 더 나쁘게 만들었어요. 1월까지 모든 단지에 수정 사항을 적용할 거고, 앞으로 베치에서 영하 34도로 시험할 거예요.

140. RAJ: You know how many vendors have told me "that part was our fault" at six in the morning? None, so thank you, Sam, seriously, because you saved the day, and Christmas.
    라지: 아침 여섯 시에 "그 부분은 우리 잘못이었다"고 말한 업체가 몇 곳이나 될 것 같아요? 하나도 없어요. 진심으로 고마워요, 샘. 오늘을 구했어요, 크리스마스도요.

141. SAM: Don't thank me, thank Lily, because she found the sensor.
    샘: 나한테 고마워하지 말고 릴리한테 해요. 센서를 찾은 건 릴리니까요.

142. RAJ: Your daughter? Lily, Tess told me about minus forty, the one temperature where both scales agree, and I'm putting that in our training manual with your name on it.
    라지: 따님이요? 릴리, 테스한테 들었어요. 영하 40, 두 온도 체계가 일치하는 유일한 온도. 그거 이름이랑 같이 우리 교육 교재에 넣을게요.

143. LILY: Thank you so much, Mr. Mehta.
    릴리: 정말 고맙습니다, 메타 씨.

144. RAJ: Call me Raj. And Lily, Helix has a co-op program for Purdue students, paid, with housing, so if you ever want a job, call me.
    라지: 라지라고 해요. 그리고 릴리, 헬릭스에도 퍼듀 학생용 코업 프로그램이 있어요. 급여에 숙소까지 주니까, 일자리 필요하면 언제든 전화해요.

145. LILY: That's very nice, but I'm applying to Ferrox, if they'll have me.
    릴리: 정말 감사해요. 근데 저 페록스에 지원할 거예요, 받아 준다면요.

146. RAJ: Ha! Sam, you're in trouble, because she negotiates like you. Go home, both of you, and merry Christmas.
    라지: 하! 샘, 큰일 났네요. 협상하는 게 당신이랑 똑같아요. 둘 다 집에 가요, 메리 크리스마스.

147. LILY: Dad, your phone buzzed with a text from Kayla.
    릴리: 아빠, 폰 울렸어. 케일라한테서 문자 왔어.

148. SAM: Read it to me, because I'm driving, very slowly.
    샘: 읽어 줘. 운전 중이거든, 아주 천천히.

149. LILY: "Merry Christmas. Defense bill passed last night. Calloway's 'study' paragraph got cut at the last minute. And a staffer on a Senate committee asked me for your number. Don't panic."
    릴리: "메리 크리스마스. 국방 법안 어젯밤 통과. 캘러웨이의 '연구' 문단은 막판에 잘렸어요. 그리고 상원 위원회 보좌관 하나가 당신 번호를 물어봤어요. 당황하지 마요."

150. SAM: "Don't panic" is what people say right before you should. Text Mom and tell her we'll be home by noon, and tell her you saved Christmas.
    샘: "당황하지 마요"는 꼭 당황해야 할 일 직전에 하는 말이야. 엄마한테 정오까지 집에 간다고 문자하고, 네가 크리스마스를 구했다고 전해.

---

## 핵심 표현 정리 (낭독하지 않음)

- **on call** — (비상 대기) 호출 대기 중인 / 004, 006
- **failover** — 페일오버(장애 시 예비 시스템으로 자동 전환) / 027–028
- **outage** — (서비스·전력) 장애, 중단 / 031
- **hunting** — 헌팅(두 제어기가 서로 보정하며 진동하는 현상) / 050
- **freeze protection** — 동결 방지(모드) / 053
- **glycol / antifreeze** — 글리콜 / 부동액 / 053–054
- **MOP (method of procedure)** — 작업 절차서 / 061–063
- **trend screen** — 추이(트렌드) 화면 / 067
- **fault code / default** — 고장 코드 / 기본값 / 077–079
- **root cause** — 근본 원인 / 090–091, 110
- **ramp** — (속도·전류를) 서서히 올리기 / 094, 106
- **Read it back to me.** — 복창해 / 116
- **First stop the bleeding. Then fix the wound.** — 먼저 피를 멈추고 그다음 상처를 고친다 / 101
- **save the day** — 위기를 구하다 / 140
- **under pressure** — 압박 속에서 / 전반

## 현안 메모 (낭독하지 않음)

- 데이터센터는 '가동률(uptime)'을 지키기 위해 냉각·전력 설비를 이중화하고, 고장 시 예비 설비로 자동 전환(failover)한다. 혹한기에는 실외 냉각 회로의 동결 방지, 센서 오작동, 장비 간 제어 충돌이 주요 위험이다. 2021년 텍사스 한파와 2022년 성탄 무렵 미국 동부 한파(엘리엇) 때는 전력망과 산업 설비 곳곳에서 동결로 인한 장애가 이어졌다.
- 섭씨와 화씨는 -40도에서 같은 값을 가진다. 일부 산업용 센서는 고장·단선 시 측정 범위의 최저값을 출력하도록 설계돼, 제어 시스템이 이를 실제 값으로 오인하는 사고가 생길 수 있다.

## 다음 화 예고 (낭독하지 않음)

- 9부 11화 New Congress. 2027년 1월 6일, 새 의회가 개원한 지 사흘. 상임위원장 명패가 바뀌고, Kayla가 Ferrox 회의실 화이트보드에 의회 지도를 그린다. "They want a witness who builds things." 그리고 1월 10일, 희토류 유예의 새 마감이 나흘 앞이다.
