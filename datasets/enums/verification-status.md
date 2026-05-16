# Enum: verification_status / حالة التحقق

**العمود / Column:** `verification_status`
**الموقع في المخطط / Schema position:** العمود 16 (الأخير) / Column 16 (last)
**النوع / Type:** نص محدود القيم (Enum)
**الحالة الافتراضية / Default value:** `draft`

**توثيق كامل / Full documentation:** [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md)

---

## القيم المقبولة / Accepted Values

### `draft`

**العربية:** مسودة أولية — الصف أُضيف ولم يُراجَع بعد.

**English:** Initial draft — row has been added but not yet reviewed.

- من يستطيع تعيينها: جميع المساهمين
- Who can assign: All contributors
- الاستخدام في production: ❌ غير مسموح
- Production use: ❌ Not allowed
- يحتاج مراجعة محامٍ: لا (بعد)
- Lawyer review required: Not yet
- يُسمح الاستشهاد به: ❌
- Citable: ❌

---

### `pending-review`

**العربية:** قيد المراجعة — الصف مُرشَّح للمراجعة القانونية وبانتظار مراجع مختص.

**English:** Pending review — row has been nominated for legal review and awaits a qualified reviewer.

- من يستطيع تعيينها: المشرفون
- Who can assign: Maintainers
- الاستخدام في production: ❌ غير مسموح
- Production use: ❌ Not allowed
- يحتاج مراجعة محامٍ: قيد التنفيذ
- Lawyer review required: In progress
- يُسمح الاستشهاد به: ❌
- Citable: ❌

---

### `reviewed`

**العربية:** مراجَع — راجع الصف شخص مختص (باحث قانوني أو أكاديمي) وأقرَّ منطقه، لكن لم يُعتمَد من محامٍ مرخَّص.

**English:** Reviewed — row has been reviewed by a qualified person (legal researcher or academic) who confirmed its logic, but not yet validated by a licensed attorney.

- من يستطيع تعيينها: المشرفون
- Who can assign: Maintainers
- الاستخدام في production: ⚠️ بتحفظ مع إفصاح
- Production use: ⚠️ With caution and disclosure
- يحتاج مراجعة محامٍ: اختياري (موصى به للمحتوى الحساس)
- Lawyer review required: Optional (recommended for sensitive content)
- يُسمح الاستشهاد به: ⚠️ مع إفصاح واضح بالحالة
- Citable: ⚠️ With explicit status disclosure

---

### `verified`

**العربية:** مُتحقَّق منه — أعلى مستوى. راجع الصف محامٍ مرخَّص في المملكة وأقرَّ دقته القانونية. يجب أن يكون `reviewed_by_lawyer = yes`.

**English:** Verified — highest tier. Row reviewed by a Saudi-licensed attorney who confirmed legal accuracy. `reviewed_by_lawyer` must be `yes`.

- من يستطيع تعيينها: المشرفون فقط (بعد تأكيد مكتوب من محامٍ)
- Who can assign: Maintainers only (after written attorney confirmation)
- الاستخدام في production: ✅ مسموح
- Production use: ✅ Allowed
- يحتاج مراجعة محامٍ: نعم (مكتمل) — `reviewed_by_lawyer = yes`
- Lawyer review required: Yes (complete) — `reviewed_by_lawyer = yes`
- يُسمح الاستشهاد به: ✅
- Citable: ✅

**شرط إلزامي / Required condition:** `reviewed_by_lawyer = yes`

---

### `deprecated`

**العربية:** متقادِم — الصف أصبح قديمًا بسبب تغيير تشريعي أو تحول في الاجتهاد القضائي. يُحتفظ به للرجوع التاريخي ولا يُستخدم في أي تطبيق.

**English:** Deprecated — row has become outdated due to legislative amendment or shift in judicial practice. Retained for historical reference; must not be used in any application.

- من يستطيع تعيينها: المشرفون فقط
- Who can assign: Maintainers only
- الاستخدام في production: ❌ محظور
- Production use: ❌ Prohibited
- يحتاج مراجعة محامٍ: غير مطلوب
- Lawyer review required: Not required
- يُسمح الاستشهاد به: ❌ محظور
- Citable: ❌ Prohibited

**متى تُستخدم / When to use:**
- صدر نظام جديد يُعدّل أو يلغي الحكم المُشار إليه
- تغيرت توجيهات جهة رقابية ذات صلة (مثل سدايا، هيئة العمل)

---

### `superseded`

**العربية:** مستبدَل — أُضيف صف آخر أكثر دقة أو تحديثًا يحلّ محل هذا الصف. يُحتفظ به للرجوع التاريخي فقط.

**English:** Superseded — a more accurate or up-to-date row has been added to replace this one. Retained for historical reference only.

- من يستطيع تعيينها: المشرفون فقط
- Who can assign: Maintainers only
- الاستخدام في production: ❌ محظور
- Production use: ❌ Prohibited
- يحتاج مراجعة محامٍ: غير مطلوب
- Lawyer review required: Not required
- يُسمح الاستشهاد به: ❌ محظور
- Citable: ❌ Prohibited

**الممارسة الموصى بها / Recommended practice:**
أضف في حقل `notes` رقم الصف البديل: `superseded by row <ID>`

---

## أخطاء شائعة / Common Errors

| خطأ ❌ | الصواب ✅ |
|--------|---------|
| `Draft` (حرف كبير) | `draft` |
| `pending_review` (شرطة سفلية) | `pending-review` (شرطة علوية) |
| `Verified` | `verified` |
| `in-review` | `pending-review` |
| `active` | `verified` أو `reviewed` |
| `inactive` | `deprecated` أو `superseded` |
| فارغ | `draft` (استخدم القيمة الافتراضية) |

---

## الملفات المرتبطة / Related Files

- [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md) — الوثيقة الكاملة لدورة الحياة
- [`datasets/schema.md`](../schema.md) — مواصفات العمود 16
- [`scripts/validate_dataset.py`](../../scripts/validate_dataset.py) — `VALID_VERIFICATION_STATUSES`
