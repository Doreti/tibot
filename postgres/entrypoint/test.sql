create table if not exists user_list
(
  id bigserial primary key,
  user_id varchar(255),
  linux varchar(255),
  git varchar(255),
  ansible varchar(255),
  postgres varchar(255),
  result varchar(255)
);
create table if not exists speciality
(
  id bigserial primary key,
  speciality varchar(255),
  need_to varchar(255)
);
create table if not exists first_table
(
  id bigserial primary key,
  qwestion varchar(255),
  answer0 varchar(255),
  answer1 varchar(255),
  answer2 varchar(255),
  answer3 varchar(255),
  type varchar(255)
);
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some linux1', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'linux');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some linux2', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'linux');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some git1', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'git');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some git2', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'git');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some ansible1', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'ansible');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some ansible2', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'ansible');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some postgres1', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'postgres');
insert into first_table (qwestion, answer0, answer1, answer2, answer3, type) values ('some postgres2', 'right answer : 1', 'bad answer : 0', 'bad answer : 0', 'bed answer : 0', 'postgres');
insert into speciality (speciality, need_to) values ('devops','linux,git,ansible,postgres');

#insert into first_table
#select data.id, case when data.id % 2 = 0 then now()::text else null end, case when data.id % 2 = 0 then 'test_string'::text else null end, null
#from generate_series(1, 100000) as data(id);
  