CREATE MIGRATION m1fu4z7yyts7opotzzzkevs7t3o4tdqbzbl52hkckhz2jghe5lbakq
    ONTO initial
{
  CREATE FUTURE simple_scoping;
  CREATE TYPE default::Semifinal {
      CREATE REQUIRED PROPERTY datetime: std::datetime;
  };
  CREATE TYPE default::Song {
      CREATE REQUIRED PROPERTY artist: std::str;
      CREATE REQUIRED PROPERTY country: std::str;
      CREATE PROPERTY eurovision_song_page: std::str;
      CREATE REQUIRED PROPERTY title: std::str;
      CREATE PROPERTY youtube_video: std::str;
  };
  CREATE TYPE default::EurovisionEdition {
      CREATE MULTI LINK semifinals: default::Semifinal;
      CREATE MULTI LINK songs: default::Song;
      CREATE REQUIRED PROPERTY hostCountry: std::str;
      CREATE PROPERTY winner: std::str;
      CREATE REQUIRED PROPERTY year: std::int16 {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
