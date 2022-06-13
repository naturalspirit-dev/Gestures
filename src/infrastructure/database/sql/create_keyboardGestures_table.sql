create table if not exists keyboardGestures (
    id integer primary key,
    shorthand text not null,
    value text not null,
    date_created text not null,
    date_updated text not null
);