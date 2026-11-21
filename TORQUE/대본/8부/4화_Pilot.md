# TORQUE — 8부 4화

## Pilot (시범사업)

> **표기 전용 정보 (낭독하지 않음)**
> - 부/화: 8부 4화 · 서사 기능: 첫 시험, 현장 문화의 충돌, 데이터의 승리
> - 배경: Helix Cloud 리킹 카운티 단지, 하역장과 3번 데이터홀 펌프실(8월 27일 목요일 밤 정비 시간대, 밤 11시~새벽 6시) → 같은 펌프실, 펌웨어 튜닝 밤샘(9월 1일 화요일 밤) → Helix 회의실, 첫 주 데이터 보고(9월 3일 목요일 오후).
> - 등장인물: Sam, Earl, Wen, Marcus, Darnell, Cole, Tess Morrow(Helix 핵심시설 운영 매니저, 신규), Brandon(Helix 야간 기술자, 신규 단역), Raj
> - 실제 사건 / 현안 태그: AI 데이터센터의 수랭식 냉각 확대, 데이터센터의 가동률(업타임) 문화와 작업 절차(MOP), 에너지 효율 측정(기준선 비교)
> - 난이도: B2 · 턴 수: 150
> - 이번 화의 핵심 표현: "maintenance window", "method of procedure (MOP)", "lockout/tagout", "uptime", "baseline", "roll back", "hunting", "the numbers speak for themselves"
> - 복선/연결: 1화 시범사업 40대 · Tess와 Earl의 존중(→12부 견습 마스터 Earl) · 펌프 라인의 토요일 근무 피로(→9화 Denise) · Raj의 "eleven campuses… and one more word"(→7화 Exclusivity)

---

## 대본

001. TESS: Mr. Washington? I'm Tess Morrow from critical facilities. You're early, since the maintenance window opens at eleven and it's only ten-fifteen.
    테스: 워싱턴 씨? 핵심시설 운영 담당 테스 모로입니다. 일찍 오셨네요. 정비 시간대는 열한 시에 열리는데 지금 열 시 십오 분밖에 안 됐어요.

002. EARL: In my world, early is on time, and on time is late.
    얼: 내 세계에선 일찍 오는 게 제시간이고, 제시간이면 늦은 거야.

003. TESS: In my world, early is fine, but nobody touches anything until eleven, not even a bolt.
    테스: 제 세계에선 일찍 오는 건 괜찮아요. 근데 열한 시 전엔 아무도 아무것도 못 만져요. 볼트 하나도요.

004. EARL: Understood. We'll unload the truck and stand around looking handsome until eleven.
    얼: 알겠어. 열한 시까지 트럭 짐 내리고 잘생긴 얼굴로 서 있을게.

005. TESS: Unloading is fine, but have you read the MOP?
    테스: 짐 내리는 건 괜찮아요. 근데 MOP 읽으셨어요?

006. EARL: The what, now?
    얼: 뭐라고?

007. TESS: The method of procedure, which is thirty-eight pages, and I sent it to Mr. Kowalski on Monday.
    테스: 작업 절차서요. 38쪽짜리인데, 월요일에 코왈스키 씨한테 보냈어요.

008. SAM: I read it, Earl, and I printed you a copy, which is in the truck under your lunch.
    샘: 제가 읽었어요, 얼. 한 부 뽑아 놨는데, 트럭에 도시락 밑에 있어요.

009. EARL: Thirty-eight pages just to change forty pumps?
    얼: 펌프 40대 바꾸는 데 38쪽이나?

010. TESS: Thirty-eight pages to change forty pumps without killing a single chip. In plain English, a MOP is a script that lists every step in order, who does it, who checks it, and how we undo it if it goes wrong.
    테스: 칩 하나 안 죽이고 펌프 40대 바꾸는 데 38쪽이요. 쉽게 말하면, MOP는 대본이에요. 모든 단계를 순서대로, 누가 하고 누가 확인하고, 잘못되면 어떻게 되돌리는지까지 적은 거죠.

011. DARNELL: A script, like in a movie?
    대넬: 대본이요? 영화처럼요?

012. TESS: It's like a movie where nobody improvises. We do step one on page four, then step two on page four, and we don't skip to page nine just because it looks easy.
    테스: 아무도 애드리브 안 하는 영화요. 4쪽 1단계 하고, 그다음 4쪽 2단계 하고, 쉬워 보인다고 9쪽으로 건너뛰지 않아요.

013. EARL: Ma'am, I've been changing motors for forty years.
    얼: 아가씨, 난 40년 동안 모터를 갈았어.

014. TESS: I believe you, and I've been keeping data centers alive for twelve. Here's the rule: every step gets read out loud, done by one person and checked by a second person, and then I sign off.
    테스: 믿어요. 그리고 전 12년 동안 데이터센터를 살려 왔어요. 규칙은 이거예요. 모든 단계를 소리 내서 읽고, 한 사람이 하고, 두 번째 사람이 확인하고, 그다음에 제가 서명해요.

015. EARL: Out loud, every single step?
    얼: 소리 내서, 모든 단계를 다?

016. TESS: Every step, and Brandon will be reading. Brandon, say hi.
    테스: 모든 단계요. 읽는 건 브랜던이 할 거예요. 브랜던, 인사해.

017. BRANDON: Hi, I'm Brandon, the night technician for Hall Three, which means I'm the guy who calls Raj at three in the morning.
    브랜던: 안녕하세요, 3번 홀 야간 기술자 브랜던이에요. 새벽 세 시에 라지한테 전화하는 사람이 저예요.

018. SAM: He told us about you, and he said you're very brave.
    샘: 얘기 들었어요. 아주 용감하다고 하더라고요.

019. BRANDON: He said "scared," didn't he?
    브랜던: '겁먹었다'고 하셨죠, 그쵸?

020. SAM: He might have said "scared," but he said it like it was a compliment.
    샘: '겁먹었다'고 했을 수도 있는데, 칭찬처럼 말했어요.

021. BRANDON: That's fair. I'm twenty-four, and Hall Three runs a customer's AI training job that's worth more than my whole town, so yeah, I'm always scared.
    브랜던: 맞는 말이에요. 전 스물넷인데, 3번 홀엔 우리 동네 전체보다 비싼 고객 AI 학습 작업이 돌아가거든요. 그러니 늘 겁나죠.

022. WEN: Good, because scared people check things twice.
    웬: 좋아요. 겁먹은 사람이 두 번 확인하거든요.

023. TESS: Dr. Liu, about the controllers, I need the serial numbers of all forty before they come in, because security will scan each one.
    테스: 리우 박사님, 제어기 말인데요, 마흔 대 전부 들어오기 전에 일련번호가 필요해요. 보안팀이 하나하나 스캔할 거라서요.

024. WEN: Marcus has the list, along with the firmware version, which is five point four, frozen on Monday.
    웬: 마커스가 목록 갖고 있어요. 펌웨어 버전도요. 5.4고, 월요일에 동결했어요.

025. MARCUS: It's forty units, serials 8801 to 8840, and the firmware hash is on the second page if your security team wants to verify it.
    마커스: 마흔 대, 일련번호 8801부터 8840까지예요. 보안팀이 확인하고 싶으면 펌웨어 해시값은 두 번째 장에 있어요.

026. TESS: They will. They verify everything, and they'd verify my mother if she visited.
    테스: 할 거예요. 그 사람들은 다 확인하거든요. 우리 엄마가 와도 확인할걸요.

027. COLE: Mr. Washington, where do you want the pallets, since the dock is pretty full?
    콜: 워싱턴 반장님, 하역장이 꽤 찼는데 팔레트 어디 둘까요?

028. EARL: Along the yellow line, Cole, ten to a row with the labels facing out.
    얼: 노란 선 따라서, 콜. 한 줄에 열 개씩, 라벨은 바깥쪽으로.

029. SAM: Cole, hey, I owe you an apology. I called you "Kyle" for a whole month.
    샘: 콜, 저기, 사과할 게 있어요. 한 달 내내 '카일'이라고 불렀죠.

030. COLE: Oh, that's okay, Mr. Kowalski. My grandma calls me Kyle too, and my uncle calls me Colin, so I answer to almost anything that starts with a K sound.
    콜: 아, 괜찮아요, 코왈스키 사장님. 우리 할머니도 카일이라고 부르고 삼촌은 콜린이라고 불러서, 저는 'ㅋ' 소리로 시작하면 거의 다 대답해요.

031. SAM: That's not the comparison I was hoping for.
    샘: 그건 내가 바랐던 비교는 아니네.

032. EARL: He's a good kid, boss. He did three weeks of Saturdays and never complained once, out loud.
    얼: 착한 애야, 사장. 3주 동안 토요일마다 나왔는데 한 번도 불평 안 했어. 소리 내서는.

033. SAM: And not out loud?
    샘: 소리 안 내서는요?

034. EARL: Not out loud, everybody complains, and that's what the parking lot is for.
    얼: 소리 안 내서는 다들 불평하지. 주차장이 그러라고 있는 거야.

035. TESS: It's eleven o'clock, and the maintenance window is open. We have seven hours. Brandon, page four, step one.
    테스: 열한 시예요. 정비 시간대 열렸고, 일곱 시간 있어요. 브랜던, 4쪽 1단계.

036. BRANDON: Step one is to confirm that Hall Three cooling loop B is on standby pumps and that loop A is carrying full load.
    브랜던: 1단계, 3번 홀 냉각 루프 B가 예비 펌프로 돌아가고 루프 A가 전체 부하를 감당하는지 확인.

037. TESS: Confirmed, I can see it on the screen. Second check?
    테스: 확인, 화면에서 보여요. 두 번째 확인?

038. WEN: Confirmed, loop A is at one hundred percent.
    웬: 확인. 루프 A 100퍼센트예요.

039. BRANDON: Step two is lockout/tagout on pump B-one, with electrical isolation at breaker panel B, position forty-two.
    브랜던: 2단계, B-1 펌프 잠금·표지. B 차단기 패널 42번 위치에서 전기 차단.

040. EARL: Lockout/tagout, finally something I understand. Darnell, you've got your lock?
    얼: 잠금·표지라, 드디어 내가 아는 게 나오네. 대넬, 자물쇠 챙겼지?

041. DARNELL: Always. It's the same lock I've had since basic training, with my name scratched on the back.
    대넬: 늘 챙기죠. 기초 훈련 때부터 쓰던 같은 자물쇠예요. 뒤에 제 이름 새겨져 있어요.

042. SAM: Darnell, explain lockout/tagout for Brandon, because he looks nervous.
    샘: 대넬, 브랜던 들으라고 잠금·표지가 뭔지 설명해 줘요. 긴장한 것 같으니까.

043. DARNELL: You turn off the power, you put your own lock on the switch, and you hang a tag with your name on it, so nobody can turn it back on but you. Your lock, your key, your life.
    대넬: 전원을 끄고, 스위치에 자기 자물쇠를 채우고, 자기 이름이 적힌 표지를 걸어요. 그러면 본인 말고는 아무도 다시 못 켜요. 내 자물쇠, 내 열쇠, 내 목숨.

044. BRANDON: I like that, "Your lock, your key, your life." Can I steal it?
    브랜던: 그거 좋네요. "내 자물쇠, 내 열쇠, 내 목숨." 써먹어도 돼요?

045. DARNELL: An Army sergeant said it first. Steal away.
    대넬: 육군 하사님이 처음 한 말이에요. 마음껏 쓰세요.

046. TESS: Stop, everybody, hands off! Who touched breaker forty-two?
    테스: 멈춰요, 다들 손 떼요! 누가 42번 차단기 만졌어요?

047. DARNELL: I did, I opened it. That's step two.
    대넬: 제가요, 내렸어요. 그게 2단계잖아요.

048. TESS: It's step two after I sign step one, and I hadn't signed. And you opened forty-two on panel A, not panel B.
    테스: 그건 제가 1단계에 서명한 다음의 2단계고, 전 아직 서명 안 했어요. 그리고 B 패널이 아니라 A 패널 42번을 내렸고요.

049. DARNELL: No. No, I—oh, no.
    대넬: 아니. 아니에요, 제가—아, 이런.

050. BRANDON: Alarm on loop A! Pump A-three is down and loop A pressure is dropping, Tess!
    브랜던: 루프 A 경보요! A-3 펌프가 멈췄고 루프 A 압력 떨어지고 있어요, 테스!

051. TESS: Close forty-two on panel A right now. Brandon, start standby pump A-seven and read me the pressure every five seconds.
    테스: A 패널 42번 지금 당장 다시 올려요. 브랜던, A-7 예비 펌프 가동하고 5초마다 압력 불러 줘.

052. EARL: Darnell, close it, close it!
    얼: 대넬, 올려, 올려!

053. DARNELL: Closed. It's closed.
    대넬: 올렸어요. 올렸어요.

054. BRANDON: A-seven is running and pressure's coming back, eighty-two percent, ninety, ninety-six, and we're back to normal.
    브랜던: A-7 돌아가고 압력 돌아와요. 82퍼센트, 90, 96, 정상으로 돌아왔어요.

055. TESS: How long was A-three down?
    테스: A-3가 얼마나 멈춰 있었어?

056. BRANDON: Forty-one seconds.
    브랜던: 41초요.

057. TESS: Forty-one seconds, and Raj told you about ninety seconds, didn't he? You just used up half of it.
    테스: 41초. 라지가 90초 얘기 했죠? 방금 그 절반을 쓰신 거예요.

058. DARNELL: Ma'am, I'm sorry, the panels look the same and I didn't check the letter.
    대넬: 죄송합니다. 패널이 똑같이 생겨서 글자를 확인 안 했어요.

059. TESS: That's why we read out loud and wait for a signature. Everybody stop. We're rolling back to step one, and nobody moves until I say so.
    테스: 그래서 소리 내서 읽고 서명을 기다리는 거예요. 다들 멈춰요. 1단계로 되돌리고, 제가 말할 때까지 아무도 움직이지 마세요.

060. EARL: Ma'am, can I say something?
    얼: 아가씨, 한마디 해도 될까?

061. TESS: You can say something, but quietly.
    테스: 하세요. 근데 조용히요.

062. EARL: My guy made a mistake, and it's on me, because I'm his foreman. I didn't read your thirty-eight pages, I read the first page and figured the rest was lawyers.
    얼: 우리 애가 실수했는데, 내 책임이야. 내가 반장이니까. 아가씨의 38쪽을 안 읽었어. 첫 장만 읽고 나머진 변호사들 얘기겠거니 했지.

063. TESS: It's not lawyers. Page eleven is what happens when a pump fails, page twelve is what happens when two fail, and page thirteen is who calls the customer.
    테스: 변호사 얘기 아니에요. 11쪽은 펌프 하나가 고장 났을 때, 12쪽은 두 대가 고장 났을 때, 13쪽은 누가 고객한테 전화하느냐예요.

064. SAM: Tess, let's take ten minutes so everybody can breathe, and then we start over from the top, out loud.
    샘: 테스, 다들 숨 좀 돌리게 10분만 쉬죠. 그다음에 처음부터 소리 내서 다시 해요.

065. TESS: Ten minutes. And Mr. Kowalski, if this happens again, I end the maintenance window, and you go home with your pumps.
    테스: 10분이요. 그리고 코왈스키 씨, 이런 일이 또 생기면 정비 시간대 끝내요. 펌프 들고 집에 가시는 거예요.

066. SAM: Understood, and Tess, that's fair, because if one of my people did that in my plant, I'd send them home too.
    샘: 알겠습니다. 그리고 테스, 그게 맞아요. 우리 공장에서 우리 직원이 그랬으면 저도 집에 보냈을 거예요.

067. DARNELL: Boss, I'm sorry. Eight years in the Army, and I flip the wrong breaker right in front of the customer.
    대넬: 사장님, 죄송해요. 군대 8년 했는데 고객 바로 앞에서 엉뚱한 차단기를 내리다니.

068. SAM: You fixed it four seconds after she yelled, and that counts too.
    샘: 테스가 소리치고 4초 만에 되돌렸잖아요. 그것도 인정해야죠.

069. EARL: Don't make him feel better, Sam. He needs to feel bad for ten minutes, and then he's fine.
    얼: 위로하지 마, 샘. 10분은 기분 나빠야 돼. 그다음엔 괜찮아.

070. EARL: Ms. Morrow, got a minute outside the hall, just the two of us?
    얼: 모로 씨, 홀 밖에서 우리 둘만 잠깐 시간 돼?

071. TESS: If this is about the MOP, I'm telling you now that the MOP doesn't change.
    테스: MOP 얘기면 미리 말씀드리는데, MOP는 안 바뀌어요.

072. EARL: It's not about the MOP, it's about 1989, when I was twenty-six at the GM plant in Moraine. A guy on my line, Ricky Hale, was clearing a jam in a press, and somebody upstairs restarted the line without checking.
    얼: MOP 얘기 아니야. 1989년, 내가 스물여섯 살에 모레인 GM 공장에 있을 때 얘기야. 우리 라인의 리키 헤일이 프레스 걸린 걸 빼고 있는데, 위에서 누가 확인도 안 하고 라인을 다시 돌렸어.

073. TESS: What happened to him?
    테스: 그분 어떻게 됐어요?

074. EARL: He lost two fingers, and he was lucky. After that, our local fought for two years to get real lockout rules, with names on the locks, and that was the union, that was us.
    얼: 손가락 두 개를 잃었는데, 그나마 운이 좋은 거였지. 그 뒤로 우리 지부가 이름 붙은 자물쇠, 진짜 잠금 규칙을 얻으려고 2년을 싸웠어. 그게 노조였고, 그게 우리였어.

075. TESS: So you know exactly why I'm like this.
    테스: 그럼 제가 왜 이러는지 잘 아시겠네요.

076. EARL: I know exactly why, because your thirty-eight pages is my lock with my name on it. I just didn't recognize it in a binder.
    얼: 딱 알지. 아가씨의 38쪽이 내 이름 붙은 자물쇠야. 바인더에 들어 있으니까 못 알아봤을 뿐이지.

077. TESS: At my first job, a pump seal failed in Virginia, and nobody had a procedure, so we lost a whole hall for nine minutes. A bank couldn't process payroll for half a day, thousands of people got paid late, and I was the night tech.
    테스: 제 첫 직장 때 버지니아에서 펌프 실링이 터졌는데, 절차서가 없어서 9분 동안 홀 하나를 통째로 날렸어요. 은행 하나가 반나절 동안 급여 처리를 못 해서 수천 명이 월급을 늦게 받았고, 제가 그 야간 기술자였어요.

078. EARL: So you were Brandon back then.
    얼: 그럼 그때 아가씨가 브랜던이었네.

079. TESS: I was Brandon, and I still have the incident report in my desk.
    테스: 제가 브랜던이었죠. 아직도 그 사고 보고서가 책상에 있어요.

080. EARL: Okay, here's my offer: you read, I check, and my guys do the work, and nobody moves without your signature. If one of mine skips a step, I'll pull him off the job myself.
    얼: 좋아, 내 제안은 이거야. 아가씨가 읽고, 내가 확인하고, 우리 애들이 하고, 아가씨 서명 없인 아무도 안 움직여. 우리 애 하나라도 단계를 건너뛰면 내가 직접 빼 버릴게.

081. TESS: You'd really do that?
    테스: 진짜 그렇게 하실 거예요?

082. EARL: Metal don't lie, Ms. Morrow. Neither do I.
    얼: 쇠는 거짓말 안 해, 모로 씨. 나도 안 하고.

083. TESS: Call me Tess, and I'll call you Earl, if that's okay.
    테스: 테스라고 불러 주세요. 괜찮으시면 저도 얼이라고 부를게요.

084. EARL: Everybody calls me Earl, except Sam when he wants something.
    얼: 다들 얼이라고 불러. 샘이 뭐 원할 때만 빼고.

085. SAM: Okay, we're back. Page four, step one, from the top.
    샘: 자, 다시 왔어요. 4쪽 1단계, 처음부터요.

086. BRANDON: Step one is to confirm loop B is on standby and loop A is carrying full load.
    브랜던: 1단계, 루프 B 예비 운전, 루프 A 전체 부하 확인.

087. EARL: Confirmed, loop A's carrying it. Tess, it's your turn to sign.
    얼: 확인. 루프 A가 버티고 있어. 테스, 서명할 차례야.

088. TESS: Signed. Step two.
    테스: 서명. 2단계.

089. BRANDON: Step two. Lockout/tagout, panel B. Bravo. Position forty-two.
    브랜던: 2단계. 잠금·표지, B 패널. 브라보. 42번.

090. DARNELL: Panel Bravo. I'm touching the letter B with my finger. Forty-two. Opening. Lock on. Tag on. My name. Darnell.
    대넬: 브라보 패널. 손가락으로 B 글자 짚고 있어요. 42번. 내립니다. 자물쇠 채움. 표지 걺. 제 이름. 대넬.

091. MARCUS: It's two in the morning, and pump B-seventeen is doing it again. Look at the speed going up and down, up and down.
    마커스: 새벽 두 시인데 B-17 펌프가 또 그래요. 속도 보세요, 올라갔다 내려갔다, 올라갔다 내려갔다 해요.

092. WEN: It's hunting, and all forty are hunting a little, but seventeen is the worst.
    웬: 헌팅이에요. 마흔 대 전부 조금씩 헌팅하는데, 17번이 제일 심해요.

093. SAM: Hunting, like deer? Earl's brother-in-law goes every November in Darke County and never hits anything.
    샘: 헌팅이요? 사슴 사냥처럼요? 얼네 처남이 매년 11월에 다크 카운티로 가는데 한 번도 못 맞혀요.

094. WEN: It's a motor that can't decide what speed it wants. In plain English, two brains are fighting over one steering wheel, because Helix's building system tells the pump, "Keep the pressure here," and our Governor is trying to do the same thing.
    웬: 원하는 속도를 못 정하는 모터예요. 쉽게 말하면 두 개의 뇌가 운전대 하나를 놓고 싸우는 거죠. 헬릭스 건물 시스템이 펌프한테 "압력 여기 맞춰"라고 하는데, 우리 거버너도 똑같은 걸 하려고 하거든요.

095. MARCUS: So when the pressure goes up a little, both of them slow the pump down until it's too slow, and then both speed it up until it's too fast.
    마커스: 그래서 압력이 조금 오르면 둘 다 펌프를 늦춰서 너무 느려지고, 그럼 둘 다 빨리 돌려서 너무 빨라지는 거예요.

096. SAM: That sounds like Erin and me parallel parking.
    샘: 에린이랑 나랑 평행 주차할 때 같네.

097. WEN: I don't know about that, but yes.
    웬: 그건 모르겠지만, 네.

098. BRANDON: The old pumps don't do this. They're loud and they waste power, but they never wiggle like that.
    브랜던: 옛날 펌프들은 이런 거 안 해요. 시끄럽고 전기를 낭비하긴 해도 저렇게 흔들리진 않아요.

099. WEN: That's because the old pumps are stupid and just do what the building says, while our pumps are smarter, so they argue.
    웬: 옛날 펌프들은 멍청해서 건물이 시키는 대로만 하니까요. 우리 펌프는 더 똑똑해서 말대꾸를 하는 거예요.

100. BRANDON: My girlfriend says that about me.
    브랜던: 제 여자 친구가 저한테 그렇게 말해요.

101. MARCUS: Is all that hunting wasting power?
    마커스: 그 헌팅 때문에 전기를 낭비하고 있어요?

102. WEN: A little. Right now we're saving about six percent, and the hunting is eating the rest, so if we fix it, we get it back.
    웬: 조금요. 지금은 6퍼센트쯤 아끼는데 나머진 헌팅이 먹고 있어요. 고치면 되찾을 수 있어요.

103. SAM: Can you change their building system?
    샘: 그쪽 건물 시스템을 바꿀 수 있어요?

104. WEN: No, because Tess would kill me, and she'd be right. We don't change the customer's brain, we change ours.
    웬: 아니요. 테스가 절 죽일 거고, 그게 맞아요. 고객의 뇌는 안 바꿔요. 우리 뇌를 바꾸죠.

105. MARCUS: So we let the building drive, and the Governor stops fighting and just follows the command and smooths it out, like a good copilot.
    마커스: 그러니까 운전은 건물한테 맡기고, 거버너는 싸움을 멈추고 명령을 따르면서 부드럽게 다듬기만 하는 거죠. 좋은 부조종사처럼요.

106. WEN: Exactly. The Governor still does what it's best at, which is the current, the heat and the low-speed efficiency, but it stops deciding the speed by itself.
    웬: 정확해요. 거버너는 여전히 자기가 제일 잘하는 전류, 열, 저속 효율을 맡고, 속도를 혼자 정하는 것만 그만두는 거예요.

107. SAM: How long will it take, honestly, Wen? The window's already closed, and Tess said nobody touches anything without her. I don't want to lose her trust in the first week.
    샘: 솔직히 얼마나 걸려요, 웬? 정비 시간대는 벌써 닫혔고, 테스가 자기 없이는 아무것도 못 만진다고 했어요. 첫 주에 그 사람 신뢰를 잃고 싶지 않아요.

108. WEN: It's two hours to write and one hour to test on one pump. If it works, we'd still need Tess's permission to load it onto the other thirty-nine.
    웬: 짜는 데 두 시간, 펌프 한 대로 시험하는 데 한 시간이요. 되더라도 나머지 서른아홉 대에 올리려면 테스 허락이 필요해요.

109. SAM: She's asleep. It's two in the morning, and she was up all night with us on Thursday, so I'm not calling her.
    샘: 그 사람 자고 있잖아요. 새벽 두 시고, 목요일에도 우리랑 밤샜으니까 전화 안 할 거예요.

110. BRANDON: Tess doesn't sleep, and she told me to text her if anything moved. She said, "Anything, Brandon."
    브랜던: 테스는 안 자요. 뭐라도 움직이면 문자하라고 했어요. "뭐라도, 브랜던"이라고요.

111. MARCUS: Doc, it's version five point four, frozen, so if we change it, it becomes five point five, which means new paperwork, a new hash and a new security scan.
    마커스: 박사님, 5.4 버전 동결이잖아요. 바꾸면 5.5가 되고, 그럼 서류도 해시도 보안 스캔도 새로 해야 돼요.

112. WEN: Then we do the paperwork, and we do it right, the way Tess does it. Marcus, write the change log while I write the code, every line.
    웬: 그럼 서류 하죠. 테스가 하는 방식대로 제대로요. 마커스, 내가 코드 짜는 동안 변경 기록 써요. 한 줄도 빼지 말고.

113. SAM: I'll get coffee. What do you want?
    샘: 커피 사 올게요. 뭐 마실래요?

114. WEN: Whatever is in the machine down the hall. It's terrible, but it's close, and at two in the morning, close beats good, which is one of the few rules of engineering nobody writes down.
    웬: 복도 끝 자판기에 있는 거요. 끔찍하지만 가까워요. 새벽 두 시엔 가까운 게 맛있는 걸 이기거든요. 공학에서 아무도 안 적어 두는 몇 안 되는 규칙 중 하나죠.

115. BRANDON: It's terrible, honestly the worst coffee in Ohio.
    브랜던: 끔찍해요. 솔직히 오하이오에서 제일 맛없는 커피예요.

116. SAM: You haven't had the coffee at our factory, where the machine sounds like a goose.
    샘: 우리 공장 커피 안 마셔 봤죠. 우리 기계는 거위 소리가 나요.

117. MARCUS: It's four-fifty a.m., and pump B-seventeen is running version five point five. Look at the speed line.
    마커스: 새벽 네 시 오십 분, B-17 펌프가 5.5 버전으로 돌아가요. 속도 선 보세요.

118. BRANDON: It's completely flat, and that's beautiful.
    브랜던: 완전히 평평해요. 아름다워요.

119. WEN: Power is down two point eight percent compared to an hour ago, which is the hunting we stopped.
    웬: 한 시간 전보다 전력이 2.8퍼센트 줄었어요. 우리가 멈춘 헌팅만큼이요.

120. SAM: So that puts us at almost nine percent.
    샘: 그럼 9퍼센트 가까이 되는 거네요.

121. WEN: That's one pump for one hour. Don't tell anyone a number yet.
    웬: 펌프 한 대에서 한 시간 돌린 거예요. 아직 아무한테도 숫자 말하지 마세요.

122. TESS: You don't have to tell me. I can see it from my kitchen, because Brandon sent me the screen at four fifty-one. Is this five point five?
    테스: 말씀 안 하셔도 돼요. 브랜던이 네 시 오십일 분에 화면을 보내 줘서 우리 집 부엌에서도 보여요. 이게 5.5예요?

123. WEN: Yes, and here is the change log, four pages, with every line we changed and why.
    웬: 네. 여기 변경 기록이요. 4쪽이고, 바꾼 모든 줄과 그 이유가 있어요.

124. TESS: Four pages for one firmware change? Earl would hate this.
    테스: 펌웨어 하나 바꾸는 데 4쪽이요? 얼이 싫어하겠네요.

125. MARCUS: Earl said, "Tell her we wrote it like a MOP," and he made us promise to say that.
    마커스: 얼 반장님이 "MOP처럼 썼다고 전해"라고 했어요. 꼭 그 말 하라고 약속하게 했고요.

126. RAJ: After one week, we have forty Ferrox pumps on loop B and forty old pumps on loop A, in the same hall with the same heat and the same load. Tess, show them.
    라지: 일주일 동안 루프 B에 페록스 펌프 마흔 대, 루프 A에 기존 펌프 마흔 대를 같은 홀, 같은 열, 같은 부하로 돌렸어요. 테스, 보여 드려요.

127. TESS: This is the baseline. In plain English, it's what the old pumps used, hour by hour, for the same job, and everything gets compared to that line.
    테스: 이게 기준선이에요. 쉽게 말하면, 같은 일을 하면서 기존 펌프가 시간마다 쓴 전력이고, 모든 걸 이 선이랑 비교해요.

128. SAM: And the blue line is us, the one that starts high and then drops off a cliff on Wednesday.
    샘: 그리고 파란 선이 우리고요. 높게 시작했다가 수요일에 절벽처럼 떨어지는 거요.

129. TESS: The blue line is you. The first day, you were only six percent better, and then on Wednesday morning it drops, which is five point five.
    테스: 파란 선이 그쪽이에요. 첫날엔 6퍼센트밖에 안 좋았는데, 수요일 아침에 뚝 떨어지죠. 그게 5.5예요.

130. RAJ: And what was the average for the week?
    라지: 그래서 일주일 평균은요?

131. TESS: Nine point four percent less energy than the baseline, with zero alarms and zero trips after Wednesday, and one early warning.
    테스: 기준선보다 에너지 9.4퍼센트 절감이고, 수요일 이후 경보 0건, 정지 0건, 그리고 조기 경고 1건이에요.

132. RAJ: A warning from whose pump?
    라지: 누구 펌프에서 경고가 나왔는데요?

133. TESS: From one of ours, an old pump on loop A sitting next to a Ferrox pump. The Ferrox controller picked up a vibration through the shared pipe and flagged it, and when we checked, the old pump's bearing was going bad.
    테스: 우리 쪽이요. 페록스 펌프 옆에 있던 루프 A의 기존 펌프인데, 페록스 제어기가 공용 배관을 타고 온 진동을 잡아서 표시했어요. 확인해 보니 기존 펌프 베어링이 상해 가고 있었어요.

134. WEN: That wasn't planned, so I'll have to think about why it worked.
    웬: 그건 계획한 게 아니라서, 왜 됐는지 생각해 봐야겠어요.

135. RAJ: So your pump told on my pump.
    라지: 그러니까 당신네 펌프가 우리 펌프를 고자질했네요.

136. EARL: Yeah, it snitched on it.
    얼: 그래, 일러바쳤지.

137. RAJ: Mr. Washington, Tess tells me you started the week as her biggest problem and ended it as her favorite person.
    라지: 워싱턴 씨, 테스 말로는 이번 주를 자기의 제일 큰 골칫거리로 시작해서 제일 좋아하는 사람으로 끝냈다던데요.

138. EARL: She exaggerates. I'm second favorite, and Brandon's first.
    얼: 과장이야. 난 두 번째로 좋아하는 사람이고, 첫 번째는 브랜던이지.

139. TESS: Brandon's my third, Earl, you're second, and Mr. Kowalski is somewhere around ninth.
    테스: 브랜던은 세 번째예요. 얼이 두 번째고, 코왈스키 씨는 아홉 번째쯤이요.

140. SAM: I'll take ninth. Honestly, after Thursday night, I expected to be somewhere below the vending machine, so ninth is a promotion.
    샘: 아홉 번째도 감사하죠. 솔직히 목요일 밤 이후론 자판기보다 아래일 줄 알았거든요. 아홉 번째면 승진이에요.

141. RAJ: Let me be honest about what nine point four means. One hall is not a campus, and one week is not ten years. My engineers will want three more weeks, and my finance team will want a model.
    라지: 9.4가 무슨 뜻인지 솔직하게 말할게요. 홀 하나가 단지는 아니고, 일주일이 10년도 아니에요. 우리 엔지니어들은 3주를 더 보자고 할 거고, 재무팀은 모델을 원할 거예요.

142. SAM: That's fair. We'll give them three more weeks and give your finance team whatever model they want. Gloria lives for that, and she'll send them a spreadsheet with eleven tabs and a color code.
    샘: 공정하네요. 3주 더 드리고, 재무팀이 원하는 모델은 뭐든 드릴게요. 글로리아가 그런 거 하려고 살거든요. 탭 열한 개에 색깔 표시까지 한 스프레드시트를 보낼 거예요.

143. RAJ: But I've been in this job for eleven years, and I've seen a lot of vendors with slides. You came with forty pumps and a man who apologizes out loud. The numbers speak for themselves.
    라지: 근데 전 이 일을 11년 하면서 슬라이드 들고 온 업체를 많이 봤어요. 당신들은 펌프 마흔 대랑 소리 내서 사과하는 사람을 데리고 왔죠. 숫자가 다 말해 주네요.

144. WEN: Give it three more weeks, and they'll speak louder, or quieter, because physics doesn't negotiate.
    웬: 3주 더 지나면 더 크게 말하거나 더 작게 말하겠죠. 물리학은 협상 안 하니까요.

145. RAJ: I've heard about that line. Okay, here's where we are: my CFO wants to see a proposal for all eleven campuses, fans and pumps, by the end of September.
    라지: 그 대사 들은 적 있어요. 좋아요, 지금 상황은 이래요. 우리 CFO가 9월 말까지 단지 열한 곳 전체, 팬하고 펌프 제안서를 보고 싶어 해요.

146. SAM: All eleven, fans and pumps? Raj, that's more motors than we've built in the whole history of the company.
    샘: 열한 곳 전부, 팬하고 펌프 다요? 라지, 그건 우리 회사 역사 전체에서 만든 것보다 많은 모터예요.

147. RAJ: All eleven. And Sam, I'll be honest with you again. When my legal team writes a contract that big, they always add one word.
    라지: 열한 곳 전부요. 그리고 샘, 또 솔직하게 말할게요. 우리 법무팀은 그렇게 큰 계약서를 쓸 때 항상 단어 하나를 넣어요.

148. SAM: What word?
    샘: 무슨 단어요?

149. RAJ: "Exclusive."
    라지: '독점'이요.

150. EARL: There it is, and I told you, boss. It's not the forty, it's what comes after the forty.
    얼: 나왔네. 내가 말했지, 사장. 문제는 40대가 아니라 40대 다음에 오는 거라고.

---

## 핵심 표현 정리 (낭독하지 않음)

- **maintenance window** — 정비 시간대 / 001, 035, 065
- **MOP (method of procedure)** — 작업 절차서(모든 단계·담당·확인·복구 방법을 적은 문서) / 005–010
- **improvise** — 즉흥적으로 하다, 애드리브하다 / 012
- **read out loud / second check / sign off** — 소리 내서 읽기 / 두 번째 확인 / 서명 승인 / 014, 037
- **lockout/tagout** — 잠금·표지(정비 중 전원을 잠그고 이름표를 거는 안전 절차) / 039–043
- **Your lock, your key, your life.** — 내 자물쇠, 내 열쇠, 내 목숨 / 043
- **roll back** — 되돌리다, 원상 복구하다 / 059
- **It's on me.** — 내 책임이다 / 062
- **hunting** — (제어) 헌팅: 목표값 주변에서 속도가 계속 오르내리는 현상 / 092–095
- **change log** — 변경 기록 / 112, 123
- **baseline** — 기준선(비교의 출발점) / 127
- **tell on / snitch on** — ~를 고자질하다, 일러바치다 / 135–136
- **The numbers speak for themselves.** — 숫자가 다 말해 준다 / 143

## 현안 메모 (낭독하지 않음)

- AI 학습용 서버 랙은 랙당 100킬로와트를 넘기도 해, 데이터센터들은 칩 위 냉각판으로 냉각수를 순환시키는 수랭식으로 빠르게 옮겨 갔다. 냉각 펌프가 수십 초만 멈춰도 칩이 과열될 수 있어, 데이터센터는 작업 절차서(MOP)와 이중 확인 문화로 가동률을 지킨다.
- 효율 개선은 같은 조건의 '기준선'과 비교해 측정한다. 전력망에서 추가 전력을 받기 어려운 상황에서 냉각 전력 절감은 곧 서버에 쓸 수 있는 전력이 된다.

## 다음 화 예고 (낭독하지 않음)

- 9월 8일 화요일. 케일라의 전화. 주 상원 선거에 나선 두 후보가 모두 페록스 공장에서 사진을 찍고 싶어 한다. 한 사람은 "오하이오 일자리"를, 한 사람은 "데이터센터가 올린 전기요금"을 말하고 싶어 한다. 휴게실에서 직원들이 갈라진다. 샘의 원칙은 하나. "Both of them can visit. Neither gets a banner."
