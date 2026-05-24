## **1. Purpose**

The purpose of this document is to define the **North Star Metrics (NSM)** for Ignis Academy. These metrics serve as the primary indicators of value creation and sustainable growth for the platform. They align product development, content strategy, and sales efforts around measurable learner and client outcomes.



## **2. Guiding Principle: Value-Driven Measurement**

Ignis Academy is a **value-driven startup**. Every measurable indicator should reflect **real value** delivered to the customer — not vanity metrics like logins or page views. The North Star Metrics focus on the _mirror of satisfaction_: when clients and learners succeed, Ignis succeeds.

Key principle:

> "We measure progress through the value experienced by our users and clients, not the volume of activity."



## **3. Key Metrics**

### 3.1. Monthly Active Users Definition

A clear definition of what an active user means is required so that we can measure true progress. The time period in which we are interested is a month. As within a month there are fluctuations of intensity of work (for an accountant, the beginning and the end of the month is more intense than the middle), we would like to average these out.

**A Monthly Active User (MAU) must satisfy at least one of the following criteria:**

1. **Completed 4 micro-lessons** in the last 30 days, OR
2. **Accumulated ≥ 60 SQS points** in the last 30 days

**Benefits of dual criteria:**
- Covers highly engaged users with fewer but deeper sessions
- Prevents penalizing long high-quality modules
- More robust MAU classification that accounts for learning intensity

### 3.2. Session Time (Minutes)

A session time is not measured by simply checking the time elapsed between the course start and completion, but actually we need to estimate the actual time spent with the course.

This has two components: the video length and the conversation with the AI Tutor.

#### 3.2.1. The Video Length

This is simply the original video length. We calculate the number of minutes assuming the user is actually watching the video. Later on, this can be adjusted if the video is skipped.

#### 3.2.2. The AI Tutor Conversation

This is more complex, as real session time can become very large if the application waits in the background for hours because a more urgent task gets priority. However, we can estimate based on the number of words the user read and the number of words they wrote.

**Assumptions (based on cognitive load studies):**
- **Reading pace:** 200 words/minute
- **Typing pace:** 35 words/minute

**Calculation:**
- **Effective reading time** = Word count / 200 minutes
- **Effective writing time** = Word count / 35 minutes

These industry-standard estimates provide session time measurements. This could be further validated with real lab tests for continuous improvement.

**Future considerations:** When multimodal interactions are added (quizzes, voice-based communication, images), we should update this metric. The essence remains the same: we need an accurate measure of how much time it takes to process the information.

### 3.3. Session Quality

Session quality is a more subjective measure where the AI helps determine how efficiently the student is learning. Although subjective, the AI tutor is better at determining this than a human.

**Session Quality Scale:**
- **User-Facing Scale:** 1-5 (for simplicity and clarity)
- **Internal Scale:** 0-100 (for aggregation, ML tuning, and finer granularity)
- **Conversion:** Multiply user-facing score by 20 to get internal score
  - Quality 1 = 20 points
  - Quality 2 = 40 points
  - Quality 3 = 60 points
  - Quality 4 = 80 points
  - Quality 5 = 100 points
  - Fraud = 0 points

**Quality Levels:**

- **0 - Fraud Detected:** No value given to the session. Detected through algorithmic signals (see Fraud Detection below).

- **1 (20 points) - Major Mistakes:** The user made significant errors, and even at the end of the session, the main ideas did not get through.

- **2-4 (40-80 points) - Average to Good Understanding:** The AI assistant asks 2-3 clarifying questions with varying complexity and, based on the user's answers, assigns a quality score. After these initial questions, the AI Tutor offers to:
  - Finish the session
  - Recommend a next module
  - Continue with additional clarifying questions or explore details further
  
  If the user continues and demonstrates improved understanding, the score can increase to 5.

- **5 (100 points) - Exceptional Understanding:** The user did an exceptional job understanding the subject. They may have had initial clarifying questions, but based on their answers, they demonstrated a thorough understanding of the lesson.

**Fraud Detection Signals:**

The system evaluates fraud using multiple algorithmic checks:

1. **Response Latency Check**
   - If user sends >120 words in <3 seconds → Flag as AI-generated

2. **Linguistic Style Mismatch**
   - Compare current answer embedding with user's average writing style
   - If cosine similarity <0.75 → Flag

3. **Complexity Analysis**
   - Sentences with >30 tokens or C2-level constructs → Flag
   - Repeated use of high-complexity phrasing → Suspicious

4. **Performance Pattern**
   - Back-to-back perfect answers with unusually fast speed → Suspicious
   - 100% accuracy combined with minimal thinking time → Flag

5. **AI-Likeness Classifier**
   - If LLM-generated probability >50% → Set Session Quality to 0

**Benefits:** Easier aggregation across thousands of sessions, consistent with standard KPI ranges, and enables finer granularity for machine learning tuning.



## **4. Key Performance Indicators (KPIs)**

### 4.1. The North Star Metric (NSM) - Session Quality Score

The Session Quality Score (SQS) represents the core value delivered to the learner through conceptual understanding, independent of time spent:

**SQS Calculation:**
```
SQS = Session Quality (0-100 internal scale)
```

**Key Principle:** Conceptual understanding matters more than speed. The SQS indicates how well a module was understood by a given user, regardless of how long it took. This reflects the reality that deep comprehension ("the pattern clicked") is more valuable than superficial speed.

**Why Time is Not a Factor:**
- **Conceptual vs. Lexical Knowledge:** Future success depends on deep understanding and pattern recognition, not memorizing facts quickly
- **Individual Learning Pace:** Some learners need more time to achieve deep understanding - this doesn't diminish the value
- **AI Pattern Recognition:** The AI tutor excels at detecting genuine understanding through conversation patterns, regardless of duration
- **Quality Over Quantity:** A 5-minute session with complete comprehension (Quality 5 = 100 points) is more valuable than a 20-minute session with poor understanding (Quality 1 = 20 points)

The SQS directly measures learning value for both the individual and the organization.

### 4.2. Other KPIs to Measure

With the foundation of SQS established, we can now measure various important metrics that provide insights into platform performance:

#### 4.2.1. Monthly Active Users in a Given Organization

This metric clearly identifies who was active and who was not. It serves as a base indicator for organization administrators to decide where to invest more resources.

#### 4.2.2. SQS per User

We can measure the total SQS for a given user, per course, and per module. This represents the value invested in a given user.

**Stakeholders:** Individual learners, organization admins, HR, and platform developers.

#### 4.2.3. SQS per Organization

An important metric (part of the North Star Metric framework) that helps in ROI calculations.

**Stakeholders:** Organization executives, finance teams, and platform leadership.

#### 4.2.4. SQS per Course and Module

Based on multiple successful sessions, we can analyze:
- How many people finished a course
- What is the average SQS
- Which parts of the module provide high value
- Where course content should be adjusted

**Minimum Data Threshold:**
- Do not compute average SQS for a module unless it has **≥ 10 completed sessions**
- Otherwise, mark as: **"Insufficient data – continue collecting"**
- This prevents misleading conclusions from small sample sizes

**Stakeholders:** Course content creators receive quality feedback on how to improve their material.

### 4.3. Quality Assessment Confidence

Every Session Quality score includes a **confidence rating (0-1)** based on AI model uncertainty:

**Confidence Levels:**
- **High:** >0.8 - AI is confident in the quality assessment
- **Medium:** 0.5-0.8 - AI has moderate confidence
- **Low:** <0.5 - AI should ask additional clarifying questions before finalizing the score

**Usage:** Low confidence scores trigger additional verification questions to ensure accurate quality assessment before recording the final session quality.

### 4.4. Learning Outcome Verification (Optional)

To bridge the gap between engagement and actual learning mastery:

**Post-Session Micro-Assessment:**
- After session completion, generate 1-3 targeted micro-questions
- Questions test core concepts from the module
- Based on correctness, adjust Session Quality ±10%
  - All correct: +10%
  - Partial correct: No adjustment
  - All incorrect: -10%

**Benefits:**
- Validates that high engagement translates to actual learning
- Provides additional data point for quality confidence
- Helps identify modules where learners engage but don't retain

**Implementation:** Optional feature that can be enabled per course or organization preference

#### 4.2.5. Monthly Spend by Organization

An important financial metric that measures how much a company is willing to invest in employee learning. This provides valuable feedback for calculating MRR (Monthly Recurring Revenue), ARR (Annual Recurring Revenue), and LTV (Lifetime Value).

**Stakeholders:** Finance teams, sales, and platform leadership.

#### 4.2.6. Organizational ROI

Based on spending and earned SQS, we can calculate an ROI index that tells both the company and the platform whether the investment is paying back optimally.

**Optimization Strategies:**
1. **Reduce investment** in learners with very low SQS (inactive or fraudulent behavior) to avoid wasted resources
2. **Increase investment** in employees who are very active and showing results by:
   - Purchasing additional courses
   - Sending them to conferences
   - Providing offline workshops

**Underlying Principle:** The Matthew Principle - "To those who have, more will be given." Focus resources on high performers who demonstrate genuine engagement and growth.

**Stakeholders:** HR, organization leadership, and L&D teams.



## **5. Metric Hierarchy Overview**

The metrics form a hierarchical structure that flows from individual learner actions up to organizational value:

```
                        NORTH STAR METRIC
                        ─────────────────
                   Organizational SQS
        (Average SQS per active user)
                             │
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
   SUPPORTING KPIS                         COMPONENT METRICS
   ───────────────                         ─────────────────
        │                                         │
        ├─ Session Quality (0-100)                ├─ Session Time (tracking only)
        │  • User-facing: 1-5                     │  ├─ Video Length
        │  • Internal: 0-100                      │  └─ AI Conversation Time
        │  • Fraud: 0                             │     ├─ Reading (200 wpm)
        │  • Confidence: 0-1                      │     └─ Writing (35 wpm)
        │                                         │
        ├─ Session Time (Minutes)                 ├─ Monthly Active Users (MAU)
        │                                         │  ├─ 4+ micro-lessons/month OR
        │                                         │  └─ ≥60 SQS points/month
        ├─ SQS per User                           │
        │  (Cumulative value)                     ├─ Monthly Spend
        │                                         │  • MRR, ARR, LTV
        │                                         │
        ├─ SQS per Module                         └─ Organizational ROI Index
        │  • Requires ≥10 sessions                   = SQS / Spend
        │                                            (Value efficiency)
        ├─ SQS per Course
        │  • Content effectiveness
        │  • Drop-off analysis
        │
        └─ Organizational ROI Index
           = Total SQS / Monthly Spend

Key Relationships:
─────────────────
• Individual SQS aggregates → Organizational SQS (total value)
• Organizational SQS ÷ Monthly Spend → ROI Index
• SQS per Module → Content quality benchmarking
• Monthly Active Users × Avg SQS → Platform health indicator
• Low confidence + Low SQS → Content review trigger
```



## **6. Data Collection & Validation**

- **Session Data:** logged automatically (AI assistant conversation + video content length).
    
- **Skill Data:** tracked through quiz results, self-assessments, and AI verification.
    
- **ROI Data:** calculated through company dashboards aggregating usage, impact, and cost.
    
- **Fraud Detection:** language style analysis, answer timing, and AI-likeness checks to ensure authentic human learning.



## **7. Reporting & Visualization**

### 7.1. Dashboard Structure

Ignis Academy will provide role-specific dashboards that present metrics in actionable, contextualized formats:

#### **7.1.1. Learner Dashboard**
- **Personal SQS Score:** Total and per-course breakdown
- **Monthly Progress:** Active status, lessons completed, streak tracking
- **Quality Trends:** Visual representation of session quality over time
- **Recommended Next Steps:** AI-driven suggestions based on performance patterns
- **Achievement Milestones:** Recognition for consistent high-quality learning

#### **7.1.2. Organization Admin Dashboard**
- **Team Overview:** Monthly active users, engagement distribution
- **SQS per Employee:** Sortable/filterable view of individual value generation
- **ROI Calculator:** Real-time calculation of organizational ROI based on spend vs. SQS
- **Investment Optimization:** Identify high-performers (invest more) and low-engagement users (intervention needed)
- **Department Comparisons:** Cross-functional performance analysis
- **Budget Allocation Insights:** Spending efficiency by team/individual

#### **7.1.3. Content Creator Dashboard**
- **Course Performance:** SQS per module and course
- **Completion Rates:** Module-by-module drop-off analysis
- **Quality Distribution:** Histogram of session quality scores (0-5)
- **Learner Feedback Patterns:** Common AI tutor conversation themes
- **Content Improvement Suggestions:** AI-generated recommendations based on low-performing modules
- **Comparative Analysis:** How courses/modules perform relative to platform averages

**Automated Feedback Loop:**

The system automatically triggers content review and generates improvement suggestions when:

**Trigger Conditions:**
- Module's **Avg SQS < 40** (low performance threshold)
- **Confidence > 0.8** (high confidence in the assessment)
- **≥ 10 users** have completed the module (minimum data threshold)

**Automated Actions:**
1. **Flag for Content Review** - Module is marked for creator attention
2. **Generate AI Insights** - System analyzes:
   - Common misconceptions from learner conversations
   - Points where learners struggled most
   - Comparison with high-performing similar modules
   - Specific sections with high drop-off rates
3. **Provide Recommendations** - Actionable suggestions such as:
   - "Consider adding more examples in section 2.3"
   - "Learners frequently ask about X - add clarification"
   - "Video pacing may be too fast at timestamp 4:30-6:15"
   - "Quiz questions should focus more on concept Y"

**Benefits:**
- Proactive content quality management
- Data-driven improvement suggestions
- Reduces manual analysis time for content creators
- Ensures continuous platform quality enhancement

#### **7.1.4. Platform Analytics (Internal)**
- **Platform Health Metrics:** Total active users, overall SQS growth trends
- **Revenue Metrics:** MRR, ARR, LTV calculations based on organizational spend
- **Fraud Detection Reports:** Flagged sessions requiring review
- **Content Quality Index:** Aggregate performance of all courses
- **Usage Patterns:** Peak learning times, popular content, engagement trends
- **Churn Risk Indicators:** Organizations or users showing declining engagement

### 7.2. Visualization Standards

All dashboards will follow consistent visualization principles:

- **Primary Metric Display:** Large, prominent SQS indicators with trend arrows (↑↓)
- **Time-Series Charts:** Line graphs for tracking progress over weeks/months
- **Comparative Views:** Bar charts for comparing users, departments, or courses
- **Distribution Analysis:** Histograms for session quality distribution
- **Heat Maps:** Activity intensity across time periods or organizational units
- **ROI Calculators:** Interactive tools with slider controls for scenario planning
- **Color Coding:** 
  - Green: High performance (Quality 4-5, High ROI)
  - Yellow: Average performance (Quality 2-3, Moderate ROI)
  - Red: Action needed (Quality 0-1, Low engagement, Fraud flags)

### 7.3. Reporting Frequency

- **Real-Time:** Individual session completion and quality scores
- **Daily:** Learner activity summaries (for engaged users)
- **Weekly:** Team performance digests (for organization admins)
- **Monthly:** Comprehensive reports with ROI calculations, budget recommendations, and strategic insights
- **Quarterly:** Executive summaries with platform-wide trends and business impact analysis

### 7.4. Export & Integration

- **Export Formats:** PDF reports, CSV data exports, API access for custom integrations
- **Integration Points:** HR systems (for performance reviews), LMS platforms, business intelligence tools
- **Automated Reports:** Scheduled delivery of key metrics to stakeholders
- **Custom Alerts:** Configurable notifications for threshold breaches (e.g., ROI drops below target, fraud detection, inactive users)



## **8. Implementation Roadmap**

### 8.1. Phase 1: Core Metrics (Months 1-3)
- Implement basic session time tracking (video + AI conversation)
- Deploy AI-based session quality scoring (0-5 scale)
- Build learner dashboard with SQS display
- Establish fraud detection baseline

### 8.2. Phase 2: Organizational Dashboards (Months 4-6)
- Create organization admin dashboard with ROI calculator
- Implement monthly active user tracking across organizations
- Deploy spending and budget allocation views
- Add comparative analysis tools

### 8.3. Phase 3: Content Optimization (Months 7-9)
- Launch content creator dashboard
- Implement course/module performance analytics
- Add AI-generated content improvement suggestions
- Deploy completion rate and quality distribution analysis

### 8.4. Phase 4: Advanced Analytics & Integration (Months 10-12)
- Build platform-wide analytics dashboard
- Implement export functionality (PDF, CSV, API)
- Integrate with HR systems and LMS platforms
- Deploy automated reporting and custom alerts
- Validate multimodal interaction tracking (voice, quiz, images)



## **9. Module Difficulty Index (MDI)**

### 9.1. Definition
Content difficulty metric based on observed learner struggle patterns.

### 9.2. Importance
Provides objective measure of module difficulty to guide content creators in maintaining appropriate challenge levels.

### 9.3. Formula
```
MDI = 100 - Avg(Session Quality) for completed sessions
```

Where Session Quality is the 0-100 internal scale.

### 9.4. Usage Rules
- **MDI > 60:** Flag for content review (too difficult)
- **40 < MDI ≤ 60:** Suggest improving clarity
- **MDI ≤ 40:** Acceptable or easy content

### 9.5. Integration
Automatically displayed on Content Creator Dashboard alongside SQS metrics.



## **10. Success Criteria**

The North Star Metric framework will be considered successful when:

1. **Measurement Accuracy:** SQS calculations are validated and trusted by stakeholders (≥95% accuracy in fraud detection, ±10% variance in time estimation)

2. **Stakeholder Adoption:** All user types actively use their respective dashboards (≥70% monthly active dashboard users)

3. **Value Demonstration:** Organizations can clearly demonstrate ROI from learning investments (average ROI index ≥1.5x)

4. **Content Improvement:** Course creators consistently improve content based on SQS feedback (≥20% improvement in low-performing modules within 6 months)

5. **Platform Growth:** SQS correlates with customer retention and revenue growth (≥0.8 correlation coefficient)



## **11. Conclusion**

The **North Star Metrics** represent Ignis Academy's unified framework for measuring success — not by surface activity, but by _authentic human learning impact_. 

> **Ignis Academy's mission:** "Turn learning data into human growth and measurable organizational performance."
