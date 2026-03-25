# Folder Cleanup Proposal
## Automotive Vehicles (AELZC441)

**Date:** 2026-01-03
**Goal:** Keep course folder clean with only YAML data files and essential documentation

---

## 📋 Current Structure (16 files)

### **Documentation Files (8):**
- `00-requirements-REVISED.md` (14K) - Current requirements
- `00-requirements.md` (11K) - Original requirements
- `01-checklist-REVISED.md` (5.5K) - Current checklist
- `01-checklist.md` (1.8K) - Original checklist
- `02-course-structure-REVISED.md` (30K) - Current structure
- `02-course-structure.md` (26K) - Original structure
- `README.md` (12K) - Main documentation
- `REVISED_STRUCTURE_PROPOSAL.md` (7.4K) - Proposal document

### **Data Files (2):**
- `03-learning-outcomes-REVISED.yaml` (47K) - **Current YAML (single source of truth)**
- `03-learning-outcomes.yaml` (42K) - Original YAML

### **Generated Files (2):**
- `03-template-REVISED.xlsx` (22K) - Can be regenerated from YAML
- `03-template.xlsx` (20K) - Can be regenerated from YAML

### **Script Files (4):**
- `convert_yaml_to_excel_REVISED.py` (6.5K) - Current converter
- `convert_yaml_to_excel.py` (6.1K) - Original converter
- `generate_excel_template.py` (15K) - Incomplete script
- `generate_template_complete.py` (26K) - Incomplete script

---

## 🎯 Proposed Clean Structure

### **Option A: Keep Only Essentials (Recommended)**

```
/Volumes/Dev/Course_Generator/
│
├── courses/
│   └── automotive-vehicles-aelzc441/
│       ├── course-data.yaml                    # RENAMED from 03-learning-outcomes-REVISED.yaml
│       ├── README.md                            # Main documentation
│       ├── requirements.md                      # RENAMED from 00-requirements-REVISED.md
│       ├── course-structure.md                  # RENAMED from 02-course-structure-REVISED.md
│       └── archive/                             # OLD FILES
│           ├── 00-requirements.md
│           ├── 01-checklist.md
│           ├── 01-checklist-REVISED.md
│           ├── 02-course-structure.md
│           ├── 03-learning-outcomes.yaml
│           ├── REVISED_STRUCTURE_PROPOSAL.md
│           └── .gitignore (ignore Excel files)
│
└── scripts/                                      # NEW COMMON FOLDER
    ├── yaml_to_excel.py                         # Generic converter (works for any course)
    └── archive/                                  # OLD SCRIPTS
        ├── convert_yaml_to_excel.py
        ├── convert_yaml_to_excel_REVISED.py
        ├── generate_excel_template.py
        └── generate_template_complete.py
```

**Result:** 4 files in course folder + archive folder

---

### **Option B: Keep Current + Archive (More Conservative)**

```
/Volumes/Dev/Course_Generator/
│
├── courses/
│   └── automotive-vehicles-aelzc441/
│       ├── 03-learning-outcomes-REVISED.yaml   # KEEP (current YAML)
│       ├── README.md                            # KEEP
│       ├── 00-requirements-REVISED.md           # KEEP
│       ├── 01-checklist-REVISED.md              # KEEP
│       ├── 02-course-structure-REVISED.md       # KEEP
│       └── archive/                             # Move old files here
│           ├── 00-requirements.md
│           ├── 01-checklist.md
│           ├── 02-course-structure.md
│           ├── 03-learning-outcomes.yaml
│           ├── 03-template-REVISED.xlsx
│           ├── 03-template.xlsx
│           └── REVISED_STRUCTURE_PROPOSAL.md
│
└── scripts/                                      # NEW COMMON FOLDER
    ├── yaml_to_excel.py                         # Generic converter
    └── archive/                                  # Move ALL scripts here
        ├── convert_yaml_to_excel.py
        ├── convert_yaml_to_excel_REVISED.py
        ├── generate_excel_template.py
        └── generate_template_complete.py
```

**Result:** 5 files in course folder + archive folder

---

## 🔧 Proposed Actions

### **Phase 1: Create Common Scripts Folder**

1. **Create:** `/Volumes/Dev/Course_Generator/scripts/`
2. **Create generic converter:** `yaml_to_excel.py`
   - Takes any course YAML as input
   - Auto-detects structure
   - Generates Excel template
   - Usage: `python scripts/yaml_to_excel.py courses/automotive-vehicles-aelzc441/course-data.yaml`

### **Phase 2: Clean Course Folder**

#### **Files to KEEP in course folder:**
- ✅ `03-learning-outcomes-REVISED.yaml` → Rename to `course-data.yaml`
- ✅ `README.md` (update paths if needed)
- ✅ `00-requirements-REVISED.md` → Rename to `requirements.md`
- ✅ `02-course-structure-REVISED.md` → Rename to `course-structure.md`
- ✅ `01-checklist-REVISED.md` → Optional (can archive)

#### **Files to MOVE to archive/ subfolder:**
- 📦 `00-requirements.md` (original)
- 📦 `01-checklist.md` (original)
- 📦 `01-checklist-REVISED.md` (if not keeping)
- 📦 `02-course-structure.md` (original)
- 📦 `03-learning-outcomes.yaml` (original)
- 📦 `REVISED_STRUCTURE_PROPOSAL.md` (proposal doc)

#### **Files to DELETE (can regenerate from YAML):**
- ❌ `03-template-REVISED.xlsx`
- ❌ `03-template.xlsx`

#### **Files to MOVE to scripts/ folder:**
- 🔧 `convert_yaml_to_excel_REVISED.py` → Use as basis for generic `yaml_to_excel.py`
- 🔧 `convert_yaml_to_excel.py` → Archive
- 🔧 `generate_excel_template.py` → Archive
- 🔧 `generate_template_complete.py` → Archive

---

## 📊 Comparison

| Aspect | Current | Option A (Clean) | Option B (Conservative) |
|--------|---------|------------------|-------------------------|
| **Files in course folder** | 16 | 4 main + archive | 5 main + archive |
| **YAML files** | 2 | 1 (renamed) | 1 (keep REVISED name) |
| **Excel files** | 2 | 0 (regenerate on demand) | 0 (in archive) |
| **Python scripts** | 4 | 0 (in common scripts/) | 0 (in common scripts/) |
| **Documentation** | 8 | 4 (clean names) | 5 (keep REVISED suffix) |
| **Archive folder** | No | Yes | Yes |

---

## 🎯 Recommended Approach: **Option A (Clean)**

### **Benefits:**
1. ✅ **Clean naming:** No "-REVISED" suffix clutter
2. ✅ **Single source of truth:** One YAML file (`course-data.yaml`)
3. ✅ **Reusable scripts:** Generic converter in common folder
4. ✅ **Easy to understand:** 4 main files, clear purpose
5. ✅ **Scalable:** Future courses follow same pattern

### **Final Structure:**
```
courses/automotive-vehicles-aelzc441/
├── course-data.yaml          ← Single source of truth (47 KB)
├── README.md                 ← How to use this course (12 KB)
├── requirements.md           ← Course requirements (14 KB)
├── course-structure.md       ← Detailed structure (30 KB)
└── archive/                  ← Historical files (reference only)
```

**Total: 4 active files (103 KB) in main folder**

---

## 🚀 Implementation Steps

### **Step 1: Create common scripts folder**
```bash
mkdir -p /Volumes/Dev/Course_Generator/scripts/archive
```

### **Step 2: Create generic YAML to Excel converter**
Create `/Volumes/Dev/Course_Generator/scripts/yaml_to_excel.py` based on `convert_yaml_to_excel_REVISED.py`

### **Step 3: Create archive folder in course**
```bash
mkdir -p /Volumes/Dev/Course_Generator/courses/automotive-vehicles-aelzc441/archive
```

### **Step 4: Move files**
```bash
# Move old documentation to archive
mv 00-requirements.md archive/
mv 01-checklist.md archive/
mv 01-checklist-REVISED.md archive/  # Optional
mv 02-course-structure.md archive/
mv 03-learning-outcomes.yaml archive/
mv REVISED_STRUCTURE_PROPOSAL.md archive/

# Move Excel files to archive (can regenerate)
mv 03-template-REVISED.xlsx archive/
mv 03-template.xlsx archive/

# Move scripts to common folder
mv convert_yaml_to_excel.py ../../scripts/archive/
mv convert_yaml_to_excel_REVISED.py ../../scripts/archive/
mv generate_excel_template.py ../../scripts/archive/
mv generate_template_complete.py ../../scripts/archive/
```

### **Step 5: Rename current files (remove REVISED suffix)**
```bash
mv 03-learning-outcomes-REVISED.yaml course-data.yaml
mv 00-requirements-REVISED.md requirements.md
mv 02-course-structure-REVISED.md course-structure.md
```

### **Step 6: Update README.md**
Update file paths to reflect new naming (no REVISED suffix)

### **Step 7: Create .gitignore in course folder**
```bash
echo "*.xlsx" > .gitignore
echo "*.xls" >> .gitignore
```

---

## 📝 Usage After Cleanup

### **To regenerate Excel template:**
```bash
cd /Volumes/Dev/Course_Generator
python scripts/yaml_to_excel.py courses/automotive-vehicles-aelzc441/course-data.yaml
# Output: courses/automotive-vehicles-aelzc441/course-template.xlsx
```

### **To edit learning outcomes:**
```bash
# 1. Edit YAML (single source of truth)
vi courses/automotive-vehicles-aelzc441/course-data.yaml

# 2. Regenerate Excel
python scripts/yaml_to_excel.py courses/automotive-vehicles-aelzc441/course-data.yaml

# 3. Upload Excel to LMS/system
```

---

## ✅ Final Checklist

After cleanup, verify:
- [ ] Course folder has only 4 main files + archive/
- [ ] YAML file renamed to `course-data.yaml`
- [ ] Scripts moved to common `scripts/` folder
- [ ] Excel files deleted (or in archive)
- [ ] README.md updated with new paths
- [ ] Generic converter script works: `python scripts/yaml_to_excel.py courses/.../course-data.yaml`
- [ ] .gitignore prevents Excel files from being committed

---

## 🤔 Questions to Consider

1. **Keep checklist file?**
   - Option A: Move to archive (completed, historical reference only)
   - Option B: Keep in main folder (track progress)

2. **Excel in archive or delete?**
   - Option A: Delete (can regenerate anytime)
   - Option B: Keep in archive (reference)

3. **Naming convention:**
   - Option A: `course-data.yaml` (generic)
   - Option B: `AELZC441-outcomes.yaml` (course-code specific)
   - Option C: Keep `03-learning-outcomes-REVISED.yaml` (descriptive)

---

**Awaiting your approval to proceed with Option A or your preferred approach.**
