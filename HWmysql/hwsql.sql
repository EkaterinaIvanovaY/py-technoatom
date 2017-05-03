

/* Вывести все года, где были фильмы, оцененные на 4, 5*/
SELECT DISTINCT year FROM Movie
INNER JOIN Rating using(mID)
INNER JOIN Reviewer using(rID)
WHERE stars>3;

/* Вывести всех обзорщиков, которые не поставили даты*/
SELECT DISTINCT name FROM Rating
INNER JOIN Reviewer using(rID)
WHERE ratingDate is null;

/*Вывести максимальный рейтинг фильма*/ 
SELECT max(avg_stars) as max_avg 
	FROM (SELECT avg(stars) as avg_stars FROM Rating 
	GROUP BY mID order by avg_stars) as avg_rating;

/*Вывести неоцененные фильмы*/
SELECT title FROM Movie
LEFT OUTER JOIN Rating using(mID)
WHERE stars is null;

/*Вывести обзорщиков на фильм GONE WITH THE WIND*/
SELECT name FROM Movie
INNER JOIN Rating using(mID)
INNER JOIN Reviewer using(rID)
WHERE title="Gone with the Wind";
 
/*Вывести разницу между мин. и макс. рейтингом фильма*/
SELECT max(avg_stars)-min(avg_stars) as max_dif 
	FROM (SELECT avg(stars) as avg_stars FROM Rating 
	GROUP BY mID order by avg_stars) as avg_rating;

