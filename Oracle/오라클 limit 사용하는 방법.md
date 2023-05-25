### 오라클 limit 사용하는 방법

> - MySql이나 postgreSQL에서 사용하는  LIMIT절을 오라클에서는 사용할 수 없다.
> - 오라클에서는 LIMIT 대신 ROWNUM을 사용하면 된다
> - 그치만 LIMIT와 ROWNUM은 사용법과 용도가 전혀 다르다

##### LIMIT

- 쿼리가 ORDER BY 절까지 모두 실행 후 해당 결과에서 원하는 행의 데이터를 가져온다.

##### ROWNUM

-  쿼리가 완전히 수행되지 않은 원 데이터의 정렬순서대로 번호를 매기긴다.

###### ※ 둘이 전혀 다른 결과가 출력된다.



```
-- MySQL
SELECT *
FROM EMP
WHERE JOB = 'SALESMANE'
ORDER BY ENAME
LIMIT 2
-- 정렬 후 결과에서 2행을 가져온다.

-- Oracle
SELECT *
FROM EMP
WHERE JOB = 'SALESMAN'
AND ROWNUM <= 2
ORDER BY ENAME
-- ROWNUM으로 2건의 데이터를 가져오는 쿼리 실행 -> MySQL과 다른 결과가 출력된다.
```

###### 오라클에서 LIMIT와 동일한 결과를 얻기 위해서는 SELECT 절로 한번 감싼 후에 ROWNUM으로 조건을 주면 LIMIT와 동일한 결과가 출력된다.

```
SELECT *
FROM (
	SELECT *
	FROM EMP
	WHERE JOB = 'SALESMANE'
	ORDER BY ENAME
	)
WHERE ROWNUM <= 2
```



##### 7번째 행에서부터 3건의 데이터를 출력하는 쿼리

```
-- MySql
SELECT *
FROM EMP
ORDER BY ENAME
LIMIT 6, 3

-- Oracle
-- 내부 쿼리에서 ROW_NUMBER()와 같은 순위 함수를 사용하여 행의 번호를 지정한 다음 해당 번호의 구간을 잘라야함.
SELECT *
FROM (
	SELECT ROW_NUMBER() OVER (ORDER BY ENAME) NUM
	, A.*
	FROM EMP A
	ORDER BY ENAME
	)
WHERE NUM BETWEEN 7 AND 9

-- 해당 쿼리에서 ORDER BY가 필요 없다면 ROWNUM 키워드를 이용하여 행의 번호를 매길 수 있다.
SELECT *
FROM (
	SELECT ROWNUM NUM
	, A.*
	FROM EMP A
	)
WHERE NUM BETWEEN 7 AND 9
```

