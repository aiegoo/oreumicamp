# 제주도 설화 기반 그루터기 스토리 구현 가이드
## Implementation Guide: Jeju Folklore-Based Tree Stump Stories

### 하례리 모델 분석 및 적용 (Based on 하례리 Case Study)

이 문서는 하례리 설화 탐방 사례를 기반으로 "오래된 그루터기의 이야기" 프로젝트에 실제 제주도 전설을 통합하는 구체적인 방법론을 제시합니다.

---

## 1. 위치 기반 설화 매핑 (GPS-Based Folklore Mapping)

### 하례리 성공 사례 분석:
- **GPS 좌표**: 33.317451, 126.597502 (하례리)
- **반경**: 5km 이내 설화 조사
- **발견된 전설**: 
  - 영천악 용 전설 (2-3km)
  - 효돈천 신선 이야기 (바로 옆)
  - 쇠소깍 비극적 사랑 (7km)
  - 원앙폭포 치유 전설 (5km)

### 우리 프로젝트 적용:
```javascript
// GPS 기반 설화 데이터베이스 구조
const folkloreDatabaseStructure = {
  location: {
    latitude: 33.317451,
    longitude: 126.597502,
    name: "하례리 그루터기",
    radius: 5000 // 5km
  },
  connectedLegends: [
    {
      name: "영천악 용 전설",
      distance: 2300, // 미터
      type: "기우제",
      connection: "나무가 용의 분노를 잠재운 자리"
    },
    {
      name: "효돈천 신선 이야기", 
      distance: 500,
      type: "풍류",
      connection: "신선들이 나무 아래서 바둑을 둔 자리"
    }
  ]
}
```

---

## 2. 설화 통합 스토리텔링 (Integrated Folklore Storytelling)

### 하례리 모델의 창작 방법론:

**원본 전설들의 요소 추출:**
- 영천악의 용 (물/가뭄/기우제)
- 효돈천의 신선 (풍류/자연/조화)  
- 쇠소깍의 사랑 (희생/변화/영원성)

**통합 서사 창작:**
"용의 분노를 잠재운 소녀의 의자" - 모든 요소를 하나의 그루터기 이야기로 연결

### 우리 팀 적용 전략:

#### 윤세정 (Content Creator) 작업 방향:
1. **제주도 오름별 설화 조사**
   - 각 하이킹 코스의 주요 오름과 연관된 전설 수집
   - GPS 좌표와 전설의 정확한 매핑
   
2. **그루터기별 맞춤 스토리 창작**
   ```markdown
   예시 스토리 구조:
   - 위치: 성산일출봉 근처 그루터기
   - 연관 설화: 성산 일출봉 설화 + 우도 소 이야기
   - 통합 내러티브: "바다를 바라보며 천년을 기다린 나무의 이야기"
   ```

3. **대화형 스토리 브랜치 설계**
   ```
   사용자: "이 나무는 왜 여기 있어요?"
   AI: "옛날 이곳에 소를 키우던 할머니가 있었는데... (우도 소 전설 연결)"
   
   선택지:
   A) 소 이야기를 더 듣고 싶어요
   B) 할머니는 어떻게 되었나요?
   C) 나무와 할머니는 어떤 관계인가요?
   ```

---

## 3. 기술 구현 방안 (Technical Implementation)

### 김지현 (Psychology/UX) + 정광식 (Frontend) 협업:

#### GPS 기반 컨텐츠 로딩:
```javascript
// 위치 감지 및 설화 매칭 시스템
class FolkloreLocationDetector {
  async detectNearbyFolklore(userGPS) {
    const nearbyLegends = await this.findLegendsInRadius(userGPS, 5000);
    const relevantStory = await this.selectMostRelevant(nearbyLegends);
    return this.adaptStoryForUser(relevantStory, userGPS);
  }
  
  adaptStoryForUser(story, userLocation) {
    // 김지현의 심리학적 연령별 적응 로직
    // 정광식의 모바일 최적화 UI
    return {
      ageAdaptedContent: this.psychology.adaptForAge(story),
      locationContext: this.geography.getVisualContext(userLocation),
      interactionMethod: this.ui.getOptimalInterface(userDevice)
    };
  }
}
```

### 박소영 (Technical Architecture) 구현 방향:

#### 오프라인 설화 데이터베이스:
```json
{
  "forestTrails": {
    "hallasan_trail_1": {
      "stumps": [
        {
          "id": "stump_001",
          "gps": [33.317451, 126.597502],
          "folklore_connections": [
            {
              "legend_id": "yeongcheon_dragon",
              "distance_meters": 2300,
              "audio_file": "dragon_legend_kr.mp3",
              "audio_file_dialect": "dragon_legend_jeju.mp3"
            }
          ]
        }
      ]
    }
  }
}
```

---

## 4. 사용자 경험 설계 (User Experience Design)

### 하례리 모델의 성공 요소 적용:

#### 이병남 (Product Manager) 경험 설계:
1. **점진적 발견 (Progressive Discovery)**
   - 하례리처럼 반경 확대하며 설화 발견
   - 첫 번째 그루터기 → 주변 전설 탐색 → 연결된 장소 방문

2. **문화적 몰입감 (Cultural Immersion)**
   ```
   체험 시나리오:
   1단계: 그루터기 발견 (GPS 자동 감지)
   2단계: 주변 설화 소개 ("5km 이내에 3개의 전설이...")
   3단계: 선택적 탐험 (사용자가 관심있는 전설 선택)
   4단계: 통합 서사 체험 (모든 전설이 연결된 새로운 이야기)
   ```

3. **실용적 관광 정보 통합**
   - 설화 + 실제 관광 정보 결합
   - 하이킹 코스 + 문화 체험 + 스토리텔링

---

## 5. 콘텐츠 제작 실전 가이드

### 단계별 콘텐츠 개발 프로세스:

#### 1주차 - 윤세정: 설화 조사 및 매핑
```markdown
과제: 제주도 주요 하이킹 코스 5곳의 설화 조사
방법: 하례리 모델 반복 적용
- GPS 좌표 중심 5km 반경 전설 수집
- 기존 전설의 핵심 요소 추출
- 그루터기 중심의 새로운 서사 구상

결과물: 
- 위치별 설화 데이터베이스
- 그루터기별 맞춤 스토리 아웃라인
```

#### 2주차 - 김지현: 심리학적 적응 설계
```markdown
과제: 연령별/성향별 스토리 적응 방안
방법: 
- 아동 심리학 관점에서 설화의 교육적 효과 분석
- 성인/가족 단위 관광객을 위한 흥미 요소 설계
- 대화형 AI의 응답 패턴 심리학적 최적화

결과물:
- 연령별 컨텐츠 적응 가이드라인
- 감정 인식 기반 스토리 분기 설계
```

#### 3주차 - 정광식: UI/UX 프로토타입
```markdown
과제: 모바일 우선 인터페이스 설계
방법:
- 하이킹 중 사용성 고려한 간편한 UI
- GPS 기반 자동 컨텐츠 로딩
- 오프라인 모드 지원

결과물:
- 인터랙티브 프로토타입
- 설화 지도 뷰어
- 음성/텍스트 선택형 인터페이스
```

#### 4주차 - 박소영: 기술 아키텍처 구현
```markdown
과제: 안정적인 백엔드 시스템 구축
방법:
- 설화 데이터베이스 설계
- GPS 기반 컨텐츠 매칭 알고리즘
- 오디오 스트리밍 최적화

결과물:
- RESTful API 서버
- 설화 데이터 관리 시스템
- 성능 모니터링 대시보드
```

---

## 6. 성공 지표 및 검증 방법

### 하례리 모델 기반 성과 측정:

1. **문화적 정확성 (Cultural Accuracy)**
   - 제주 문화 전문가 검토 통과율: >90%
   - 현지 주민 피드백 만족도: >4.0/5.0

2. **사용자 참여도 (User Engagement)**
   - 설화 완독률: >70%
   - 위치 기반 스토리 완주율: >60%
   - 재방문 의향: >50%

3. **교육적 효과 (Educational Impact)**
   - 제주 문화 이해도 증진: 사전/사후 비교
   - 자연 환경 보호 의식 향상 측정

---

## 다음 단계 실행 계획

### 즉시 시작 가능한 작업:

1. **이병남 (PM)**: 제주 문화원/관광공사 연락하여 설화 자료 수집 허가 요청
2. **윤세정 (Content)**: 하례리 외 4개 주요 관광지 설화 1차 조사 시작
3. **김지현 (UX)**: 설화 스토리텔링의 아동 심리학적 효과 문헌 조사
4. **정광식 (Frontend)**: GPS 기반 웹앱 기본 프레임워크 셋업
5. **박소영 (Backend)**: 설화 데이터베이스 스키마 설계 시작

### 1주일 내 목표:
- 하례리 모델을 5개 관광지에 확대 적용한 기초 조사 완료
- 팀 역할별 첫 번째 프로토타입 산출물 검토
- 제주도 현지 협력 파트너 1곳 이상 컨택 완료

---

**프로젝트 슬로건**: *"제주의 천년 설화, 현대의 디지털 기술로 되살리다"*

*Traditional Jeju legends, revived through modern digital storytelling* 🌳🏝️