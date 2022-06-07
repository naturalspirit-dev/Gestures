create table if not exists keyboardGestures (
    id integer primary key,
    shorthand text not null,
    value text not null
);