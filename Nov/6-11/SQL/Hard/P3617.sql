with process_1 as (
select
	student_id,
	COUNT(distinct subject) total_subject,
	SUM(hours_studied) total_study_hours
from
	study_sessions
group by
	student_id
),
process_2 as (
select
	student_id,
	session_date, 
	lead(session_date) over(partition by student_id order by session_date) - session_date diff_date
from
	study_sessions
)
select
	p.student_id,
	s.student_name,
	s.major,
	COUNT(distinct p.subject) cycle_length,
	MAX(pro.total_study_hours) total_study_hours
from
	study_sessions p
inner join process_1 pro on
	p.student_id = pro.student_id
inner join students s on
	p.student_id = s.student_id
inner join study_sessions p1 on
	p.student_id = p1.student_id
	and p.subject = p1.subject
	and p.session_date < p1.session_date
	AND p1.session_date - p.session_date BETWEEN pro.total_subject AND pro.total_subject * 2
where
	exists (
	select
		1
	from
		process_2 pp
	where
		p.student_id = pp.student_id
		and p.session_date = pp.session_date
		and diff_date < 3 )
group by
	p.student_id,
	s.student_name,
	s.major
having
	COUNT(distinct p.subject) = ( select total_subject from process_1 ps where ps.student_id = p.student_id ) AND COUNT(distinct p.subject) > 2
order by
	cycle_length desc,
	total_study_hours desc