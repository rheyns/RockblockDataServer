drop table if exists rockblock;
create table rockblock (
  id integer primary key autoincrement,
  date text not null,
  telemetry blob not null
);
