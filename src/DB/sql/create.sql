CREATE TABLE "Users" (
  "id" SERIAL PRIMARY KEY,
  "username" varchar(60),
  "password" varchar(64)
);

CREATE TABLE "History" (
  "search_id" SERIAL PRIMARY KEY,
  "id" int,
  "time" timestamp,
  "language" varchar,
);

CREATE TABLE "Sentence_history" (
  "sentence_id" SERIAL PRIMARY KEY,
  "sentence" varchar,
  "search_id" int
);

CREATE TABLE "Languages" (
  "language_id" SERIAL PRIMARY KEY,
  "language" varchar
);

CREATE TABLE "Articles" (
  "article_id" SERIAL PRIMARY KEY,
  "language_id" int,
  "article_link" varchar,
  "article_metadata" varchar
);

CREATE TABLE "Article_sentence" (
  "sentence_id" SERIAL PRIMARY KEY,
  "article_id" int,
  "sentence" varchar
);

ALTER TABLE "History" ADD FOREIGN KEY ("id") REFERENCES "Users" ("id");

ALTER TABLE "Sentence_history" ADD FOREIGN KEY ("search_id") REFERENCES "History" ("search_id");

ALTER TABLE "Articles" ADD FOREIGN KEY ("language_id") REFERENCES "Languages" ("language_id");

ALTER TABLE "Article_sentence" ADD FOREIGN KEY ("article_id") REFERENCES "Articles" ("article_id");