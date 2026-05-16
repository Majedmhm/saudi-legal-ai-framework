# خريطة التقاطعات / Cross-Reference Map

**Saudi Legal AI Framework** — دليل الروابط بين مكونات المشروع

هذه الخريطة تُظهر الروابط بين ملفات المشروع المختلفة. الهدف: أن يعرف أي مساهم بالضبط أين يحتاج أن يُحدِّث عند إضافة مكوّن جديد أو تغيير مكوّن موجود.

This map shows the relationships between project files. The goal: every contributor knows exactly what needs updating when a component is added or changed.

---

## كيف تستخدم هذه الخريطة؟ / How to Use This Map

**سيناريو شائع / Common scenario:**

> "غيّرت هيكل تقرير `skills/contract-review.md` — ماذا أُحدِّث أيضًا؟"
> "I changed the report structure in `skills/contract-review.md` — what else needs updating?"

1. ابحث عن الملف الذي غيّرته في الجداول أدناه.
2. اقرأ عمود **"الملفات المرتبطة"** — كل ملف فيه يحتاج مراجعة.
3. تحقق من أن التغيير منسجم في كل الملفات المرتبطة.

1. Find the file you changed in the tables below.
2. Read the **"Related Files"** column — each listed file needs review.
3. Verify the change is consistent across all related files.

---

## 1. Skills ← → Sources / المهارات ← → المصادر

| Skill | المهارة | Related Sources | ملاحظة |
|---|---|---|---|
| `skills/contract-review.md` | مراجعة العقود | `sources/civil-transactions-law.md` · `sources/labor-law.md` · `sources/companies-law.md` · `sources/pdpl.md` · `sources/commercial-courts.md` | المصدر الرئيسي لهيكل التقرير في §8 |
| `skills/labor-law-analysis.md` | تحليل نظام العمل | `sources/labor-law.md` | نظام العمل م/51 هو المرجع الأساسي |
| `skills/commercial-dispute.md` | النزاعات التجارية | `sources/commercial-courts.md` · `sources/saudi-laws.md` | يتقاطع مع نظام التحكيم م/34 |
| `skills/compliance-check.md` | فحص الامتثال | `sources/pdpl.md` · `sources/labor-law.md` · `sources/companies-law.md` | يغطي 3 أنظمة رئيسية |
| `skills/legal-drafting.md` | الصياغة القانونية | `sources/civil-transactions-law.md` · `sources/saudi-laws.md` | يستند لمبادئ نظام المعاملات المدنية |

---

## 2. Skills ← → Prompts / المهارات ← → قوالب المطالبات

| Skill | Related Prompts | طبيعة العلاقة |
|---|---|---|
| `skills/contract-review.md` | `prompts/review-contract.md` | الـ prompt يُطبِّق هيكل §8 من الـ skill — أي تغيير في الهيكل يستلزم تحديث الـ prompt |
| `skills/labor-law-analysis.md` | `prompts/review-contract.md` (قالب عقد العمل) | يستخدم الـ prompt نفسه مع سياق العمل |
| `skills/commercial-dispute.md` | `prompts/risk-analysis.md` | تحليل المخاطر يعتمد على منطق النزاعات التجارية |
| `skills/compliance-check.md` | `prompts/risk-analysis.md` | فحص الامتثال يُخرَج كتقرير مخاطر |
| `skills/legal-drafting.md` | `prompts/draft-notice.md` | صياغة الإشعارات تعتمد مبادئ الـ skill |

---

## 3. Skills ← → Examples / المهارات ← → الأمثلة التطبيقية

| Skill | Related Examples | ملاحظة |
|---|---|---|
| `skills/contract-review.md` | `examples/employment-contract-review.md` · `examples/nda-review.md` · `examples/saudi-contract-review-demo.md` | الـ demo هو التطبيق الكامل لـ §8 |
| `skills/labor-law-analysis.md` | `examples/employment-contract-review.md` | المثال يُطبِّق تحليل نظام العمل |
| `skills/commercial-dispute.md` | — | لا يوجد مثال تطبيقي بعد |
| `skills/compliance-check.md` | — | لا يوجد مثال تطبيقي بعد |
| `skills/legal-drafting.md` | — | لا يوجد مثال تطبيقي بعد |

---

## 4. Sources ← → Regulations / المصادر ← → الأنظمة

| Source File | Regulation | Royal Decree | صيغة الاستشهاد الرسمية |
|---|---|---|---|
| `sources/civil-transactions-law.md` | نظام المعاملات المدنية | م/191 1443هـ | `Saudi Civil Transactions Law (Royal Decree M/191 1443H)` |
| `sources/labor-law.md` | نظام العمل | م/51 1426هـ | `Saudi Labor Law (Royal Decree M/51 1426H)` |
| `sources/companies-law.md` | نظام الشركات | م/132 1443هـ | `Saudi Companies Law (Royal Decree M/132 1443H)` |
| `sources/commercial-courts.md` | نظام المحاكم التجارية | م/93 1441هـ | `Commercial Courts Law (Royal Decree M/93 1441H)` |
| `sources/pdpl.md` | نظام حماية البيانات الشخصية | م/19 1443هـ | `Personal Data Protection Law PDPL (Royal Decree M/19 1443H)` |
| `sources/saudi-laws.md` | نظرة عامة (جميع الأنظمة) | — | مرجع عام — يُشير لـ `regulation-index.md` |
| `sources/regulation-index.md` | **جميع الأنظمة العشرة** | متعددة | **المصدر الرسمي الوحيد لصيغ الاستشهاد** |

> الأنظمة المسجَّلة في `regulation-index.md` لكن **بدون** ملف `sources/` مخصص بعد:
> - Saudi Arbitration Law (م/34 1433H)
> - Commercial Agency Law (م/11 1382H)
> - Intellectual Property Protection Law (م/41 1424H)
> - Saudi Bankruptcy Law (م/50 1439H)
> - Electronic Transactions Law (م/18 1428H)

---

## 5. Judicial Corpus ← → Indexing ← → Extraction / المجموعة القضائية ← → الفهرسة ← → الاستخراج

هذه الطبقات الثلاث تعمل بتسلسل صارم — لا يبدأ الاستخراج قبل اكتمال الفهرسة.

These three layers work in strict sequence — extraction does not begin before indexing is complete.

| Layer | Directory | Related Files | ملاحظة |
|-------|-----------|---------------|--------|
| **Judicial Corpus** | `sources/judicial-decisions/1435/` | `sources/judicial-decisions/README.md` | 14 ملف PDF مسحوب ضوئيًا — لا يمكن استخراج نصها آليًا |
| **Corpus Index** | `datasets/judicial-index/` | `datasets/judicial-index/schema.md` · `judicial-corpus-index.csv` · `README.md` | الفهرسة اليدوية لأقسام الـ PDF — مدخل الاستخراج |
| **Judicial Extraction** | `datasets/judicial-reasoning/` | `datasets/judicial-reasoning/schema.md` · `example-extraction.md` · `extraction-guidelines.md` | 19 حقلًا — يبدأ بعد اكتمال الفهرسة |

### تبعيات الطبقات / Layer Dependencies

```
sources/judicial-decisions/1435/*.pdf
        │
        ▼  (فهرسة يدوية — read PDF table of contents)
datasets/judicial-index/judicial-corpus-index.csv
        │
        ▼  (اختيار الأقسام ذات extraction_priority = high/medium)
        │
        ▼  (استخراج يدوي — requires human reading of PDF pages)
datasets/judicial-reasoning/{extraction files}
        │
        ▼  (تحقق — reviewed → verified)
skills/ و datasets/ الرئيسية
```

> **ملاحظة OCR / OCR Note:** ملفات الـ PDF مسحوبة ضوئيًا (scanned images) — استخراج النص الآلي غير ممكن بالأدوات الحالية. طبقة OCR مخططة في المستقبل. الاستخراج الحالي يدوي بالكامل.

### عند إضافة قسم جديد للفهرس / When Adding a New Index Section

```
✅ أضف صفًا في:              datasets/judicial-index/judicial-corpus-index.csv
✅ اتبع هيكل الـ index_id:  IDX-{year}-{vol}-{seq}
✅ اقرأ start_page/end_page: من فهرس الـ PDF يدويًا — ضع 0 إذا لم تتحقق
✅ أضف TO VERIFY:            لأي حقل غير مؤكد
✅ لا تضع reasoning هنا:    الاستخراج يتم في datasets/judicial-reasoning/ فقط
```

### عند إضافة استخراج قضائي / When Adding a Judicial Extraction

```
✅ تأكد من وجود صف في الفهرس أولًا:   datasets/judicial-index/judicial-corpus-index.csv
✅ اتبع المخطط:                        datasets/judicial-reasoning/schema.md (19 حقلًا)
✅ اقرأ دليل الاستخراج:                datasets/judicial-reasoning/extraction-guidelines.md
✅ أخفِ جميع البيانات الشخصية:         [صاحب العمل] · [العامل] · [المحكمة X] بدلًا من الأسماء الحقيقية
✅ أضف verification_status = draft:    دائمًا عند الإنشاء
✅ لا تستخرج من حكم غير قابل للقراءة: توقف وأضف ملاحظة في الفهرس
```

---

## 6. Contract Datasets ← → Enums / قواعد البيانات ← → القيم المضبوطة

| Dataset / Column | Enum File | القيم المقبولة |
|---|---|---|
| `*` → `risk_level` | `datasets/enums/risk-levels.md` | `critical` · `high` · `medium` · `low` |
| `*` → `contract_type` | `datasets/enums/contract-types.md` | 11 نوعًا — راجع الملف |
| `*` → `clause_category` | `datasets/enums/clause-categories.md` | 14 فئة — راجع الملف |
| `*` → `industry` | `datasets/enums/industries.md` | 12 قطاعًا — راجع الملف |

**ينطبق على جميع ملفات CSV / Applies to all CSV files:**
- `datasets/saudi-contract-risk-dataset.csv`
- `datasets/examples/*.csv`
- `datasets/contributions/**/*.csv`
- `datasets/build/*.generated.csv`

---

## 7. Contract Datasets ← → Scripts / قواعد البيانات ← → السكربتات

| File / Path | Script | الدور |
|---|---|---|
| `datasets/saudi-contract-risk-dataset.csv` | `scripts/validate_dataset.py` | التحقق من صحة الـ master dataset |
| `datasets/examples/*.csv` | `scripts/validate_dataset.py` | التحقق من الأمثلة |
| `datasets/contributions/**/*.csv` | `scripts/validate_dataset.py` | يُشغَّل قبل كل PR |
| `datasets/contributions/**/*.csv` | `scripts/build_dataset.py` | المدخل — يُدمج المساهمات |
| `datasets/build/*.generated.csv` | `scripts/build_dataset.py` | المخرج — يُولِّد هذا الملف |
| `datasets/build/*.generated.csv` | `scripts/validate_dataset.py` | التحقق من الملف المُولَّد بعد البناء |
| `datasets/enums/*.md` + `datasets/schema.md` | `scripts/validate_dataset.py` | المصادر التوثيقية للـ enums — أي تغيير يستلزم تحديث الثوابت في السكربت |

---

## 8. Workflows ← → GitHub Actions / سير العمل ← → الإجراءات الآلية

| Workflow File | Trigger | ما الذي يُشغَّل | الملفات المرتبطة |
|---|---|---|---|
| `.github/workflows/validate-datasets.yml` | `push` · `pull_request` | `scripts/validate_dataset.py` على master + examples | `datasets/saudi-contract-risk-dataset.csv` · `datasets/examples/*.csv` |
| `.github/workflows/auto-label.yml` | `pull_request` (opened/sync/reopened) | `actions/labeler@v5` | `.github/labeler.yml` |

**ملاحظة:** `validate-datasets.yml` **لا** يشغّل الـ validation على `datasets/contributions/` تلقائيًا. المساهمون يُشغّلون الـ validation يدويًا قبل فتح الـ PR.

---

## 9. قواعد الصيانة / Maintenance Rules

> كل تغيير في ملف رئيسي يستلزم تحديث الخريطة وتحديث الملفات المرتبطة به.

Every change to a core file requires updating this map and the files linked to it.

---

### عند إضافة Skill جديد / When Adding a New Skill

```
✅ أضف الـ skill في:             skills/<domain>.md
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جداول 1 و 2 و 3)
✅ افتح Issue لإضافة مصدر:       sources/<regulation>.md (إذا لم يكن موجودًا)
✅ افتح Issue لإضافة prompt:     prompts/<task>.md (إذا لم يكن موجودًا)
✅ افتح Issue لإضافة مثال:       examples/<scenario>.md
✅ تحقق من regulation-index.md:  هل الأنظمة المرتبطة مسجَّلة؟
```

---

### عند إضافة Source جديد / When Adding a New Source

```
✅ أضف الـ source في:            sources/<regulation>.md
✅ سجّل في الـ registry:         sources/regulation-index.md (إلزامي)
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جدول 4)
✅ حدّث الـ skills المرتبطة:     أضف إشارة للـ source في الـ skill المناسب
✅ حدّث CONTRIBUTING.md:         إذا كان النظام الجديد يؤثر على معايير الاستشهاد
```

---

### عند إضافة Enum جديد / When Adding a New Enum Value

```
✅ حدّث ملف الـ enum:            datasets/enums/<type>.md
✅ حدّث validate_dataset.py:     أضف القيمة الجديدة للثابت المناسب (VALID_*)
✅ حدّث datasets/schema.md:      اذكر القيمة الجديدة في وصف العمود
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جدول 5)
```

---

### عند إضافة نوع عقد / When Adding a New Contract Type

```
✅ حدّث:  datasets/enums/contract-types.md
✅ حدّث:  scripts/validate_dataset.py → VALID_CONTRACT_TYPES
✅ حدّث:  datasets/schema.md
✅ أنشئ مجلد مساهمة (إن لزم): datasets/contributions/<domain>/
✅ حدّث هذه الخريطة:  docs/cross-reference-map.md (جداول 5 و 6)
```

---

### عند تغيير Output Format / When Changing the Output Format

هذا التغيير الأكثر تأثيرًا — يجب تحديث سلسلة كاملة:

This is the highest-impact change — requires updating a full chain:

```
skills/<domain>.md §8 (أو القسم المعني بالهيكل)
    ↓  يُعدَّل أولًا — المصدر الأساسي
prompts/<related>.md
    ↓  يُعدَّل ثانيًا — يعكس الهيكل الجديد
examples/<related>.md
    ↓  يُعدَّل ثالثًا — يُطبِّق الهيكل الجديد
docs/cross-reference-map.md
    ↓  يُحدَّث أخيرًا
```

> لا تُغيِّر الـ prompt أو الـ example دون أن تُغيِّر الـ skill أولًا.
> Never change the prompt or example without first changing the skill.

---

### عند إضافة GitHub Workflow جديد / When Adding a New GitHub Workflow

```
✅ أضف الـ workflow في:          .github/workflows/<name>.yml
✅ حدّث .github/labeler.yml:    إذا كان يتعامل مع مسارات ملفات جديدة
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جدول 7)
✅ حدّث README.md إذا لزم:      أضف badge أو ذكر للـ workflow
```

---

## ملخص التبعيات الحرجة / Critical Dependency Summary

```
regulation-index.md  ←── مرجع لـ ── sources/*.md ←── مرجع لـ ── skills/*.md
                                                                      ↓
                                                              prompts/*.md
                                                                      ↓
                                                              examples/*.md

datasets/enums/*.md  ←── يُحكم ──── validate_dataset.py ←── يُشغَّل بواسطة ── CI workflow
datasets/schema.md   ←── يوثّق ──── datasets/**/*.csv

sources/judicial-decisions/*.pdf  ──▶  judicial-index/judicial-corpus-index.csv
                                                  │
                                                  ▼  (بعد اكتمال الفهرسة)
                                   datasets/judicial-reasoning/{extractions}
                                                  │
                                                  ▼  (بعد التحقق)
                                         skills/ و datasets/ الرئيسية
```

---

*آخر تحديث / Last updated: 2026-05-17 — يعكس حالة المشروع في v0.2 (judicial corpus + indexing + extraction layers)*

*حدّث هذا التاريخ عند كل مراجعة للخريطة. / Update this date on every map revision.*
