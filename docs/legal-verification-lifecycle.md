# دورة حياة التحقق القانوني / Legal Verification Lifecycle

**الإصدار / Version:** 1.1
**تاريخ الإصدار / Release date:** 2026-05-16
**ينطبق على / Applies to:** جميع صفوف مجموعة بيانات مخاطر العقود السعودية
**Applies to:** All rows in the Saudi Contract Risk Dataset

---

## 1. مقدمة / Introduction

يصف هذا المستند دورة حياة التحقق القانوني لكل صف في مجموعة البيانات.
This document describes the legal verification lifecycle for every row in the dataset.

كل صف يمر بمراحل متسلسلة من المسودة إلى التحقق الكامل أو التقاعد؛ حقل `verification_status` هو المتتبِّع الرسمي لهذه المرحلة.

Every row progresses through sequential stages from draft to full verification or retirement; the `verification_status` field is the authoritative tracker of this stage.

**لماذا يهم هذا الحقل؟ / Why does this field matter?**

| السبب | الأثر |
|-------|-------|
| يُميّز المحتوى الموثوق من المسودات | يمنع استخدام بيانات غير مراجَعة في production |
| يُوثّق مسار المراجعة | يُتيح تتبع من راجع ومتى |
| يُوجّه نماذج اللغة | يمنعها من الاستشهاد بمحتوى غير مُعتمَد |
| يُتيح الحوكمة | يحدد متى تصبح البيانات قديمة أو منسوخة |

---

## 2. الحالات / States

### draft — مسودة

**المعنى:** الصف أُضيف حديثًا ولم يُراجَع بعد. محتواه قد يكون صحيحًا لكنه لم يخضع لأي تحقق خارجي.

**Meaning:** Row was recently added and has not yet been reviewed. Content may be accurate but has not undergone any external verification.

**من يستطيع استخدامها:** المساهمون عند إضافة صفوف جديدة — هذه الحالة الافتراضية.

**Who can use it:** Contributors when adding new rows — this is the default state.

**ينطبق على حالات:**
- صفوف أُنشئت آليًا أو يدويًا بدون مراجعة
- محتوى مُستخرَج من مصادر تجريبية لم تُتحقق

---

### pending-review — قيد المراجعة

**المعنى:** الصف مُرشَّح للمراجعة القانونية وبانتظار تحقق محامٍ أو مراجع مختص.

**Meaning:** Row has been nominated for legal review and is awaiting verification by a qualified attorney or reviewer.

**من يستطيع استخدامها:** المشرفون والمساهمون الذين يُرشّحون صفوفًا للمراجعة.

**Who can use it:** Maintainers and contributors who nominate rows for review.

**ينطبق على حالات:**
- الصف أُضيف إلى قائمة انتظار المراجعة الرسمية
- طُلب من محامٍ مرخَّص مراجعة الصف

---

### community-reviewed — مراجَع مجتمعيًا

**المعنى:** راجع الصف باحث أو ممارس أو مساهم موثوق في المشروع وأقرَّ منطقه. هذه الحالة ليست اعتمادًا قانونيًا نهائيًا من محامٍ مرخَّص — بل هي إقرار مجتمعي يُعزّز جودة المحتوى قبل التحقق الرسمي.

**Meaning:** Row has been reviewed by a researcher, practitioner, or trusted project contributor who confirmed its logic. This status is not a final legal approval from a licensed attorney — it is a community endorsement that strengthens content quality before formal verification.

**من يستطيع استخدامها:** المشرفون بعد اكتمال مراجعة مجتمعية موثَّقة.

**Who can use it:** Maintainers after a documented community review is complete.

**المسار الأساسي:** `draft` → `community-reviewed` → `verified`

**Primary path:** `draft` → `community-reviewed` → `verified`

**يختلف عن `reviewed` في:** `community-reviewed` يُشير صراحةً إلى مراجعة مجتمعية (باحث أو مساهم)؛ `reviewed` يُستخدم للمراجعات المُنجَزة عبر المسار الرسمي (pending-review → reviewed).

**Differs from `reviewed` in:** `community-reviewed` explicitly denotes a community-sourced review (researcher or contributor); `reviewed` is used for reviews completed through the formal channel (pending-review → reviewed).

**ينطبق على حالات:**
- صف راجعه باحث قانوني مستقل وأقرّ دقته المنطقية
- صف راجعه ممارس ذو خبرة في المجال وأكد اتساقه مع الممارسة
- صف قدَّم عليه مساهم موثوق ملاحظات تفصيلية مقبولة

---

### reviewed — مراجَع

**المعنى:** راجع الصف شخص مختص (غير محامٍ مرخَّص بالضرورة) — مثل باحث قانوني أو أكاديمي. المحتوى أُقرَّ منطقيًا لكنه لم يصل لمستوى التحقق القانوني الرسمي.

**Meaning:** Row has been reviewed by a qualified person (not necessarily a licensed attorney) — such as a legal researcher or academic. Content has been logically approved but has not reached formal legal verification.

**من يستطيع استخدامها:** المشرفون بعد مراجعة من شخص مختص.

**Who can use it:** Maintainers after review by a qualified person.

**يختلف عن `verified` في:** لم يُراجَع من محامٍ مرخَّص في المملكة.

**Differs from `verified` in:** Not reviewed by a Saudi-licensed attorney.

---

### verified — مُتحقَّق منه

**المعنى:** الحالة الأعلى مستوى. راجع الصف محامٍ مرخَّص في المملكة العربية السعودية وأقرَّ دقته القانونية. يوافق هذا الحقل تمامًا على `reviewed_by_lawyer = yes`.

**Meaning:** Highest-tier status. Row has been reviewed by a Saudi-licensed attorney who confirmed its legal accuracy. This status corresponds exactly to `reviewed_by_lawyer = yes`.

**من يستطيع استخدامها:** المشرفون فقط — بعد تأكيد مكتوب من محامٍ مرخَّص.

**Who can use it:** Maintainers only — after written confirmation from a licensed attorney.

**شرط ضروري:** يجب أن يكون `reviewed_by_lawyer = yes` في نفس الصف.

**Required condition:** `reviewed_by_lawyer` must be `yes` in the same row.

---

### deprecated — مُتقادِم

**المعنى:** الصف لا يزال موجودًا في المجموعة لكنه أصبح قديمًا — مثلًا بسبب تعديل تشريعي أو تغيير في الاجتهاد القضائي. لا يُستخدم في تطبيقات الإنتاج.

**Meaning:** Row still exists in the dataset but has become outdated — e.g., due to legislative amendment or shift in judicial practice. Must not be used in production applications.

**من يستطيع استخدامها:** المشرفون فقط، عند اكتشاف تغيير تشريعي يُؤثر على دقة الصف.

**Who can use it:** Maintainers only, upon discovering a legislative change that affects row accuracy.

**ينطبق على حالات:**
- صدر نظام جديد يتعارض مع المحتوى
- تغيرت توجيهات هيئة حكومية ذات صلة

---

### superseded — مُستبدَل

**المعنى:** الصف استُبدل بصف آخر أكثر دقة أو تحديثًا. يُحتفظ به للرجوع التاريخي فقط.

**Meaning:** Row has been replaced by a more accurate or up-to-date row. Retained for historical reference only.

**من يستطيع استخدامها:** المشرفون فقط، عند إضافة نسخة مُحدَّثة من الصف.

**Who can use it:** Maintainers only, when an updated version of the row is added.

**الممارسة الموصى بها:** أضف رقم الصف البديل في حقل `notes` — مثال: `superseded by row 47`.

**Recommended practice:** Add the replacement row ID in the `notes` field — e.g., `superseded by row 47`.

---

## 3. مصفوفة التحقق / Verification Matrix

| الحالة / Status | المعنى باختصار | من يعيّنها | يُسمح في production | يحتاج مراجعة محامٍ | يُسمح الاستشهاد به |
|----------------|---------------|------------|--------------------|--------------------|-------------------|
| `draft` | مسودة أولية | المساهمون | ❌ | لا (بعد) | ❌ |
| `pending-review` | قيد المراجعة | المشرفون | ❌ | قيد التنفيذ | ❌ |
| `community-reviewed` | مراجَع مجتمعيًا ★ | المشرفون | ⚠️ بتحفظ مع إفصاح | لم يكتمل | ⚠️ مع إفصاح |
| `reviewed` | مراجَع (غير محامٍ) | المشرفون | ⚠️ بتحفظ | اختياري | ⚠️ مع إفصاح |
| `verified` | مُتحقَّق قانونيًا | المشرفون فقط | ✅ | نعم (مكتمل) | ✅ |
| `deprecated` | متقادم | المشرفون فقط | ❌ | غير مطلوب | ❌ |
| `superseded` | مستبدَل | المشرفون فقط | ❌ | غير مطلوب | ❌ |

★ المسار الأساسي الجديد: `draft` → `community-reviewed` → `verified`

**Verification Matrix (English)**

| Status | Brief meaning | Who assigns | Production use | Lawyer review needed | Citable |
|--------|--------------|-------------|---------------|---------------------|---------|
| `draft` | Initial draft | Contributors | ❌ | Not yet | ❌ |
| `pending-review` | Awaiting review | Maintainers | ❌ | In progress | ❌ |
| `community-reviewed` | Community-reviewed ★ | Maintainers | ⚠️ With caution | Not yet complete | ⚠️ With disclosure |
| `reviewed` | Reviewed (non-lawyer) | Maintainers | ⚠️ With caution | Optional | ⚠️ With disclosure |
| `verified` | Legally verified | Maintainers only | ✅ | Yes (complete) | ✅ |
| `deprecated` | Outdated | Maintainers only | ❌ | Not required | ❌ |
| `superseded` | Replaced | Maintainers only | ❌ | Not required | ❌ |

★ Primary new path: `draft` → `community-reviewed` → `verified`

---

## 4. انتقالات الحالة / State Transitions

**المسار الأساسي الجديد / New Primary Path:**

```
draft ──────────────────────► community-reviewed ──────────────► verified
                                                                      │
                                                                      ▼
                                                                deprecated
                                                                      │
                                                               superseded
```

**المسار البديل (الرسمي) / Alternate Formal Path:**

```
draft ──► pending-review ──► reviewed ──► verified
```

**القواعد / Rules:**

- الحالة الافتراضية عند الإضافة: `draft`
- الانتقال من `draft` إلى `community-reviewed`: بعد مراجعة باحث أو ممارس أو مساهم موثوق ★
- الانتقال من `community-reviewed` إلى `verified`: بعد تأكيد محامٍ مرخَّص + تعيين `reviewed_by_lawyer = yes`
- الانتقال من `draft` إلى `pending-review`: قرار المشرف (المسار الرسمي البديل)
- الانتقال من `pending-review` إلى `reviewed`: بعد مراجعة مختص غير محامٍ (المسار الرسمي البديل)
- الانتقال من `reviewed` إلى `verified`: بعد تأكيد محامٍ مرخَّص + تعيين `reviewed_by_lawyer = yes`
- الانتقال إلى `deprecated`: عند تغيير تشريعي
- الانتقال إلى `superseded`: عند إضافة صف بديل

★ `community-reviewed` لا تُعيَّن ذاتيًا — يعيّنها المشرف بعد التحقق من اكتمال المراجعة المجتمعية.

---

## 5. معيار البيانات الوصفية / Metadata Standard

### الحقول ذات العلاقة / Related fields

| الحقل | العلاقة بـ verification_status |
|-------|-------------------------------|
| `reviewed_by_lawyer` | يجب أن يكون `yes` عند الحالة `verified` |
| `notes` | يجب أن يشير للصف البديل عند الحالة `superseded` |
| `source_type` | يؤثر على المسار: `published_case` يتسارع إلى reviewed |

### قواعد الاتساق / Consistency rules

1. إذا كانت `verification_status = verified` فيجب أن تكون `reviewed_by_lawyer = yes`
2. إذا كانت `reviewed_by_lawyer = yes` فيجب أن تكون `verification_status` في `{community-reviewed, reviewed, verified}`
3. إذا كانت `verification_status = superseded` يجب ذكر ID البديل في `notes`
4. إذا كانت `verification_status = community-reviewed` فيجب أن تكون `reviewed_by_lawyer = no` (المراجعة المجتمعية لا تُعادل مراجعة محامٍ)

### Consistency rules (English)

1. If `verification_status = verified`, then `reviewed_by_lawyer` must be `yes`
2. If `reviewed_by_lawyer = yes`, then `verification_status` should be in `{community-reviewed, reviewed, verified}`
3. If `verification_status = superseded`, the replacement row ID should appear in `notes`
4. If `verification_status = community-reviewed`, then `reviewed_by_lawyer` must be `no` (community review does not equal attorney review)

---

## 6. دليل المساهم / Contributor Guide

### عند إضافة صف جديد

لا تحتاج لتحديد أي شيء غير `draft` — هذا هو المطلوب دائمًا:

```csv
...,reviewed_by_lawyer,notes,verification_status
...,no,,draft
```

### عند تقديم مراجعة مجتمعية (المسار الأساسي الجديد)

أرسل PR يتضمن:
- `verification_status = community-reviewed`
- `reviewed_by_lawyer = no` (المراجعة المجتمعية لا تُعادل مراجعة محامٍ)
- في وصف الـ PR: اذكر هوية المراجع (باحث / ممارس / مساهم موثوق) وملخص ما راجعه

```csv
...,reviewed_by_lawyer,notes,verification_status
...,no,,community-reviewed
```

### عند تحديث صف موجود تغيّر الحكم النظامي فيه

1. غيّر `verification_status` إلى `deprecated`
2. أو أضف صفًا جديدًا محدَّثًا وغيّر القديم إلى `superseded`
3. أضف في `notes` للصف القديم: `superseded by row <ID>`

### عند تقديم دليل من محامٍ مرخَّص

أرسل PR يتضمن:
- `reviewed_by_lawyer = yes`
- `verification_status = verified`
- في وصف الـ PR: اذكر مؤهلات المراجع وتاريخ المراجعة

---

## 7. العلاقات المرجعية / Related References

| الملف | العلاقة |
|-------|---------|
| [`datasets/enums/verification-status.md`](../datasets/enums/verification-status.md) | القيم الرسمية للـ enum |
| [`datasets/schema.md`](../datasets/schema.md) | مواصفات العمود 16 |
| [`docs/cross-reference-map.md`](cross-reference-map.md) | خريطة التبعيات الكاملة |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | قواعد المساهمة العامة |
