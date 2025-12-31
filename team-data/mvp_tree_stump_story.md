# MVP Specification: The Story of the Old Stump

## Product Overview
- **Title:** The Story of the Old Stump
- **Goal:** Deliver an interactive digital experience that shares the story and lessons of the old tree stump, engaging users emotionally and intellectually.

## Product Owner/Management Perspective
- **Target Audience:** Children, educators, and families interested in nature, storytelling, and life lessons.
- **Core Value:** Empathy, environmental awareness, and the beauty of aging and memory.
- **Key Features:**
  - Interactive storytelling (text, audio, visuals)
  - User choices that affect story flow
  - Simple, accessible UI/UX
  - Progress tracking or bookmarking
- **Success Metrics:**
  - User engagement (time spent, choices made)
  - Positive feedback from users/educators
  - Repeat usage or sharing

## Technical Perspective
- **Platform:** Web application (responsive for desktop/tablet/mobile)

- **Machine Learning & NLP Integration:**
  - Personalized Storytelling: Use NLP to adapt story text and narration to the user's reading level, interests, or emotional state.
  - Interactive Dialogue: Implement simple conversational AI so users can ask the stump questions and receive context-aware, story-driven responses.
  - Sentiment Analysis: Analyze user input (text or voice) to adjust story tone or suggest branches that match the user's mood.
  - Content Generation: Use generative AI to expand story branches or create new endings based on user choices and feedback.

- **Tech Stack:**
  - Frontend: React.js (or similar)
  - Backend: Node.js/Express (optional for user data)
  - Data: JSON or simple DB for story content and user progress
  - Machine Learning/NLP: Python (Hugging Face Transformers, spaCy, or OpenAI API for NLP tasks)

- **MVP Scope:**
  - **Location-Aware Landing Page**: GPS-based story selection from Jeju folklore database
  - **Folklore-Driven Story Flow**: 2-3 interactive choices based on actual legends
    - Example: 영천악 용 전설 → 효돈천 신선 → 쇠소깍 사랑 이야기 연결
  - **Contextual Audio Narration**: Jeju dialect options with cultural pronunciation
  - **Minimalist Design**: Nature-inspired UI reflecting Jeju's volcanic landscape
  - **Intelligent Folklore Q&A**: 
    - "이 나무가 왜 여기 있어요?" → Local legend-based answers
    - "용이 정말 살았나요?" → Cultural context + imaginative responses
    - GPS coordinate integration for location-specific folklore

- **Future Extensions:**
  - More story branches
  - User accounts and saving progress
  - Richer media (animations, sound effects)
  - Advanced conversational AI for deeper interaction
  - Adaptive storytelling using user sentiment and preferences
  - Voice-based interaction and narration using speech-to-text and text-to-speech

## Team Integration & Role Assignments

### 5-Member Team Structure:
1. **김지현 (Psychology/UX)**: 
   - Research and prototyping of folklore-based user experiences
   - Child psychology research for age-appropriate storytelling
   - User interaction prototyping with location-based narratives
2. **박소영 (Civil Engineering/Audio)**: 
   - Design UX and data preprocessing for folklore mapping
   - GIS-based location analysis (ArcGIS/QGIS, Google Earth)
   - Spatial data integration for GPS-based storytelling
3. **윤세정 (Social Welfare/Creative)**: 
   - Product Owner and Project Management
   - Documentation and stakeholder communication
   - Content strategy and folklore integration oversight
4. **이병남 (Business Management/PM)**: 
   - Data pipeline architecture and LangChain integration
   - Product packaging and DevOps implementation
   - ML/NLP infrastructure and deployment automation
5. **정광식 (Business Management/Frontend)**: 
   - Coding and LLM management
   - Frontend development and AI integration
   - Mobile optimization and conversational AI implementation

### Development Phases:
- **Phase 1 (Weeks 1-2)**: Research & Planning (김지현, 이병남)
- **Phase 2 (Weeks 3-4)**: Core Development (정광식, 박소영)
- **Phase 3 (Weeks 5-6)**: Content & Gaming Features (윤세정, 김지현)
- **Phase 4 (Weeks 7-8)**: Testing & Deployment (Full team)

### Jeju Island Integration:
- **Target Location**: Oreum/Doole-gil hiking trails (following 하례리 model)
- **Folklore Research Methodology**: 
  - GPS coordinate-based folklore mapping within 5km radius
  - Integration of existing legends (영천악 용 전설, 쇠소깍 사랑 이야기, 효돈천 신선 설화)
  - Creation of synthetic stories combining multiple local legends
- **Location-Specific Implementation**:
  - Each tree stump location mapped to specific Jeju folklore
  - Original legends + AI-generated connecting narratives
  - Interactive dialogue referencing actual place names and traditions
- **Cultural Elements**: 
  - Jeju dialect integration for authentic experience
  - Traditional storytelling formats (설화 structure)
  - Local geographic features as story anchors
- **Tourism Enhancement**: Digital companion linking nature tours to cultural heritage

## Gaming & Reward System Implementation

### Mobile Camera Integration (하례리 Model Implementation):
- **Folklore Location Recognition**: Camera identifies specific locations (영천악, 효돈천, 쇠소깍)
- **Story-Specific Photo Quests**: 
  - "영천악에서 용의 모습을 찾아보세요" (찾기 게임)
  - "효돈천에서 신선이 앉았을 법한 바위를 찍어보세요"
  - "쇠소깍의 장군바위를 찾아 사랑 이야기를 완성하세요"
- **AR Folklore Overlays**: 
  - Virtual dragon appearing over 영천악 during story moments
  - Traditional Korean clothing on historical figures
  - Interactive 한라산 spirit guides
- **GPS-Based Story Progression**: Movement between locations triggers new folklore chapters

### Card-Based Discovery Gaming System:
**Adapted from solo exploration RPG mechanics for Jeju folklore discovery:**

**Discovery Mechanics:**
- **Finding New Story Elements**: Roll dice to determine number of folklore elements to discover
- **Revelation Method**: Roll to determine how you encounter each story element:
  - 1: **Arduous Discovery** - Challenging hike or climb required
  - 2 **Sudden Encounter** - Story element appears unexpectedly 
  - 5-6: **Restful Observation** - Discovered while taking a break

**Story Element Categories (Card Suits):**
- **♦ Diamonds - Living Folklore**: Legendary creatures, spirits, people from stories
- **♣ Clubs - Sacred Nature**: Ancient trees, mystical plants, natural shrines
- **♥ Hearts - Cultural Heritage**: Stone monuments, abandoned structures, ritual sites
- **♠ Spades - Natural Phenomena**: Volcanic formations, springs, caves, rock formations

**Location Context (Card Ranks):**
- **A**: In tall silver grass fields (억새밭)
- **2**: Under moonlight on Hallasan
- **3**: By a mountain stream
- **4**: In a deep volcanic canyon
- **5**: Atop an Oreum (volcanic cone)
- **6**: On a snowy peak
- **7**: Near volcanic vents
- **8**: On coastal cliffs
- **9**: In lava tube caves
- **10**: On rocky outcroppings
- **J**: In windswept grasslands
- **Q**: By the ocean shore
- **K**: At elevated viewpoints

**Gameplay Integration:**
- Players draw digital "cards" as they explore Jeju locations
- Each card combination generates a unique folklore discovery
- Journal entries recorded in the app create personal story collections
- Completed "planets" (locations) unlock new Jeju regions to explore

### Digital Badge System (Cultural Heritage Focus):
- **설화 Master**: Complete all folklore-based story paths
- **Jeju Language Learner**: Unlock Jeju dialect pronunciation achievements
- **Cultural Bridge Builder**: Successfully connect multiple local legends
- **Sacred Site Visitor**: Visit all folklore locations within story narrative
- **Storyteller**: Create and share personal endings to traditional tales

## Open Questions
- What age range should the language and choices target? (김지현 to research)
- Should narration be professional or AI-generated? (박소영 to evaluate options)
- How will user feedback be collected? (이병남 to design feedback system)
- Which Jeju hiking trails should be prioritized? (Team field research needed)
- How to handle offline functionality during hikes? (정광식 to implement PWA features)

---
Add more details, questions, or ideas below as the team iterates!
