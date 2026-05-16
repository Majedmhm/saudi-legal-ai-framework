# Real-Time APIs الحكومية السعودية
# Saudi Government Real-Time APIs

**المرجع / Reference:** `https://open.data.gov.sa/ar/pages/real-time-api`
**النوع / Type:** توثيق معماري — لا integration code حالياً
**Architecture documentation — no integration code at this stage**

---

## ⚠️ تحذير / Warning

> هذا الملف توثيق معماري مستقبلي **فقط**.
> لا يتضمن أي كود integration أو connectors أو استدعاءات API.
> APIs الحكومية **لا تُعدَّل ولا تُفسَّر** النصوص القانونية الرسمية، ولا تُغني عن الرجوع إلى هيئة الخبراء (boe.gov.sa) أو الجريدة الرسمية للنص الرسمي الساري.
>
> This file is **future architectural documentation only**.
> It contains no integration code, connectors, or API calls.
> Government APIs do **not** amend or interpret official legal texts and do not replace the Bureau of Experts (boe.gov.sa) or the Official Gazette for authoritative current text.

---

## 1. ما هي Real-Time APIs الحكومية / What Are Government Real-Time APIs

منصة data.gov.sa تُتيح — إضافةً إلى مجموعات البيانات الثابتة — واجهات برمجية (APIs) تتيح الوصول الآلي المباشر إلى بيانات حكومية يتم تحديثها بشكل دوري أو فوري.

Beyond static datasets, the data.gov.sa platform provides programmatic APIs enabling automated direct access to government data updated periodically or in real time.

**الخصائص الجوهرية / Key characteristics:**

| الخاصية | الوصف |
|---------|-------|
| **الوصول** | HTTP REST — يستلزم مفتاح API أو تسجيل |
| **التنسيق** | JSON / CSV — قابل للمعالجة الآلية |
| **التحديث** | دوري أو شبه فوري حسب المجموعة |
| **الترخيص** | بيانات حكومية مفتوحة — تحقق من شروط الاستخدام لكل مجموعة |
| **الجهة المشغِّلة** | هيئة الحكومة الرقمية |

---

## 2. لماذا قد تكون مفيدة للمشروع / Why Useful for This Project

المشروع حالياً يعمل بمحتوى وثائقي ثابت. مستقبلًا — خاصةً في Phase 4 (MCP Integration) — يمكن لـ APIs أن تُضيف قيمة في ثلاثة محاور:

The project currently operates on static documentation. In the future — particularly in Phase 4 (MCP Integration) — APIs can add value across three axes:

### أ. التحديث التلقائي / Automatic Updates
بدلاً من الاعتماد على مساهمين يُدخلون التغييرات يدويًا، يمكن لـ API أن تُنبّه تلقائيًا عند:
- صدور تعديل على نظام مُستشهَد به في datasets
- تغيير في إحصاء قضائي مُشار إليه في sources

Instead of relying on contributors to manually enter changes, an API can automatically alert when a regulation cited in the dataset is amended, or when a judicial statistic referenced in sources changes.

### ب. التحقق المرجعي / Reference Validation
التحقق آليًا من أن مرجعًا قانونيًا مُدرَجًا في المشروع لا يزال ساريًا وصحيح الصيغة.

Automatically verify that a legal reference listed in the project is still current and correctly formatted.

### ج. إثراء السياق / Context Enrichment
إضافة بيانات إحصائية حديثة كسياق داعم لمحتوى المشروع دون استبداله.

Adding up-to-date statistical data as supporting context for project content without replacing it.

---

## 3. الفرق بين المصادر / Source Type Comparison

| النوع | المثال | الموثوقية | الاستخدام المناسب |
|-------|--------|-----------|------------------|
| **Official APIs** | data.gov.sa REST API | عالية — مصدر رسمي مرخَّص | إحصاء، بيانات وصفية، تحقق مرجعي |
| **Open Datasets** | ملفات CSV من data.gov.sa | عالية — لكن قد تكون قديمة | تحليل نمط، بناء مجموعات بيانات |
| **Unofficial Scraping** | جمع بيانات من مواقع دون إذن | ❌ غير مقبول | **محظور في هذا المشروع** |

**القاعدة:** لا يُستخدم في هذا المشروع إلا مصادر رسمية مرخَّصة أو بيانات مفتوحة بترخيص صريح.

**Rule:** Only officially licensed sources or explicitly licensed open data are used in this project.

---

## 4. Potential Future Use Cases

استخدامات محتملة في مراحل لاحقة من المشروع (Phase 4 وما بعدها):

Potential uses in later project phases (Phase 4 and beyond):

### judicial metadata ingestion — استيعاب البيانات الوصفية القضائية
- جلب قائمة المحاكم التجارية والعمالية وتخصصاتها تلقائيًا
- تحديث بيانات اختصاص المحاكم عند إنشاء محاكم جديدة
- ربط اسم المحكمة بموقعها الجغرافي وتخصصها للاستفسارات

Automatically fetching the list of commercial and labor courts with their specializations, updating court jurisdiction data when new courts are established, and linking court names to locations and specializations for queries.

### regulation updates — تحديثات الأنظمة
- الاستعلام الدوري عن أحدث إصدار لنظام مُسجَّل في `regulation-index.md`
- إشعار تلقائي عند اكتشاف تعديل على نظام مُستشهَد به
- مقارنة رقم المرسوم المُدرَج في المشروع برقم المرسوم الساري

Periodic querying for the latest version of a regulation registered in `regulation-index.md`, automatic notification when an amendment to a cited regulation is detected, and comparing the decree number in the project with the current operative decree number.

### legal statistics — إحصاءات قانونية
- إحصاءات القضايا التجارية والعمالية سنويًا كخلفية لتقييم أهمية البنود
- معدلات التسوية الودية مقابل الأحكام في نزاعات نوع معين
- مؤشرات الأداء القضائي (متوسط مدة الفصل)

Annual commercial and labor case statistics as background for assessing clause significance, amicable settlement vs. judgment rates for specific dispute types, and judicial performance indicators (average time-to-resolution).

### compliance signals — إشارات الامتثال
- اكتشاف تغييرات في متطلبات التقارير التنظيمية (PDPL، نطاقات)
- مؤشرات على تحوّل في أولويات التطبيق الرقابي
- تحديثات في قوائم الجهات الرقابية المعتمدة

Detecting changes in regulatory reporting requirements (PDPL, Nitaqat), indicators of shifts in regulatory enforcement priorities, and updates to lists of approved supervisory bodies.

### government reference validation — التحقق المرجعي الحكومي
- التحقق من أن رقم المرسوم الملكي المُدرَج في dataset صحيح ومطابق للسجل الرسمي
- التحقق من أن اسم الجهة الحكومية لا يزال صحيحًا (بعد دمج وزارات أو إعادة تسميتها)
- التحقق من أن الرابط الرسمي المُدرَج لا يزال صالحًا

Verifying that a Royal Decree number in the dataset is correct and matches the official record, that a government body name is still current (after ministry mergers or renames), and that an official link is still valid.

---

## 5. Safety & Governance

### عدم الاعتماد على APIs كمصدر قانوني نهائي
APIs تُوفّر بيانات وصفية وإحصائية — **لا تُنشئ قاعدة قانونية ولا تُفسَّر الأنظمة**.
النص الرسمي المُعتمَد دائمًا هو: هيئة الخبراء (boe.gov.sa) والجريدة الرسمية (uqn.gov.sa).

APIs provide metadata and statistics — they **do not create legal rules or interpret regulations**.
The authoritative official text is always: Bureau of Experts (boe.gov.sa) and Official Gazette (uqn.gov.sa).

### ضرورة verification
أي بيانات مُستخلَصة من API قبل إدراجها في المشروع يجب أن:
- تبدأ بحالة `verification_status = draft`
- تُراجَع من مختص قبل الترقية إلى `reviewed`
- لا ترقى إلى `verified` إلا بتأكيد مكتوب من محامٍ مرخَّص

Any data extracted from an API before inclusion in the project must start at `verification_status = draft`, be reviewed by a specialist before advancing to `reviewed`, and only reach `verified` with written confirmation from a licensed attorney.

### احترام rate limits
- لا تُرسَل طلبات API بتكرار يتجاوز الحد المسموح من الجهة المُشغِّلة
- تُحفظ الردود محليًا (cache) لتجنب الطلبات المكررة غير الضرورية
- يُوقَف الاستعلام فورًا عند استلام رمز خطأ 429 أو ما يماثله

Do not send API requests at a rate exceeding the operator's permitted limit, cache responses locally to avoid unnecessary repeated requests, and immediately stop querying on receiving a 429 or equivalent error code.

### عدم تخزين بيانات حساسة
- لا تُخزَّن بيانات تُعرِّف أفرادًا أو شركات بعينها
- لا تُدرَج في المشروع بيانات تتضمن معلومات شخصية أو تجارية سرية
- كل ما يُدرَج في datasets يجب أن يكون مجمَّعًا (aggregate) ومُجرَّدًا

Do not store data identifying specific individuals or companies, do not include personal or commercially confidential information in the project, and ensure all dataset entries are aggregate and abstracted.

### عدم استخدام scraping غير رسمي
- **محظور تمامًا** في هذا المشروع جمع البيانات من مواقع حكومية بدون إذن صريح
- فقط APIs المرخَّصة رسميًا أو مجموعات البيانات المفتوحة بترخيص واضح
- يُوثَّق رابط الترخيص لكل مصدر قبل استخدامه

**Strictly prohibited** in this project: collecting data from government websites without explicit permission. Only officially licensed APIs or clearly licensed open datasets are permitted. The license link for each source must be documented before use.

---

## 6. Planned Future Architecture

التصور المعماري المبدئي لمسار API في Phase 4 — **لا كود حالياً، تصور فقط**:

Initial architectural vision for the API pipeline in Phase 4 — **no code at this stage, conceptual only**:

```
┌─────────────────────────────────────────────────────────────┐
│                     API Source Layer                        │
│  data.gov.sa REST API  ·  boe.gov.sa  ·  regulatory feeds  │
└──────────────────────────────┬──────────────────────────────┘
                               │ licensed API calls only
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      Ingestion Layer                        │
│  rate-limited fetch  ·  response caching  ·  format parse  │
└──────────────────────────────┬──────────────────────────────┘
                               │ raw structured data
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Normalization Layer                      │
│  map to schema columns  ·  enum validation  ·  dedup       │
└──────────────────────────────┬──────────────────────────────┘
                               │ schema-compliant rows
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Verification Layer                       │
│  verification_status = draft  ·  human review flag         │
│  cross-check against regulation-index.md                   │
└──────────────────────────────┬──────────────────────────────┘
                               │ draft rows flagged for review
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  Legal Classification Layer                 │
│  clause_category  ·  risk_level  ·  related_regulation     │
│  reviewed by specialist → status: reviewed / verified      │
└──────────────────────────────┬──────────────────────────────┘
                               │ classified, verified content
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     Reasoning Layer                         │
│  skills/  ·  prompts/  ·  datasets/                        │
│  judicial reasoning patterns  ·  dispute signals           │
│  AI assistant context enrichment                           │
└─────────────────────────────────────────────────────────────┘
```

**ملاحظات معمارية / Architectural notes:**

- كل طبقة مستقلة — يمكن تطوير أي منها دون المساس بالأخرى
- الـ verification layer هي الحاجز الحارس: لا شيء يصل لـ reasoning layer دون مراجعة بشرية
- المخرج النهائي دائمًا وثائق منظَّمة — لا بيانات خام

Each layer is independent — any can be developed without affecting others. The verification layer is the guardian gate: nothing reaches the reasoning layer without human review. Final output is always structured documentation — never raw data.

---

## 7. الملفات المرتبطة / Related Files

| الملف | العلاقة |
|-------|---------|
| [`sources/open-data-judicial-sources.md`](../sources/open-data-judicial-sources.md) | المصدر التكميلي (open datasets) من نفس المنصة |
| [`sources/regulation-index.md`](../sources/regulation-index.md) | سجل الأنظمة — الهدف الأول لـ reference validation |
| [`docs/legal-verification-lifecycle.md`](legal-verification-lifecycle.md) | معيار `verification_status` للبيانات المُستخلَصة |
| [`ROADMAP.md`](../ROADMAP.md) | Phase 4 (MCP Integration) — السياق الزمني لهذا التصور |
