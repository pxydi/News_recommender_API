create table documents (
  id integer primary key autoincrement,
  category text not null,
  title text not null,
  doc_text text not null
);
