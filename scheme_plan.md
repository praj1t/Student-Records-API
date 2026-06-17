# V3 Database Schema Plan

## students
- id: primary key
- name: required string
- created_at: timestamp
- updated_at: timestamp

## subjects
- id: primary key
- name: required unique string
- created_at: timestamp
- updated_at: timestamp

## marks
- id: primary key
- student_id: foreign key to students.id
- subject_id: foreign key to subjects.id
- score: number between 0 and 100
- created_at: timestamp
- updated_at: timestamp

Rules:
- one student can have many marks
- one subject can have many marks
- one student should only have one mark per subject

## grade_audit_logs
- id: primary key
- student_id: foreign key to students.id
- subject_id: foreign key to subjects.id
- old_score: previous score
- new_score: updated score
- reason: optional text
- changed_at: timestamp

Rules:
- every mark update should create an audit log
- audit logs should not be edited after creation

## Derived Values

Do not store average or letter_grade as normal columns.
They should be calculated from marks when generating a report.