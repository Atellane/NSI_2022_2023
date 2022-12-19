<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Analyse données forumaire</title>
	</head>
	<body>

		<p>Liste des données récupérées en Get :</p>

	<?php
	if (empty($_GET))
		echo 'VIDE!!!';
	else{
		foreach($_GET as $key => $value)
		{
			echo '<b>Key</b> = ' . $key . ' / ';
			echo '<b>Value</b> = ' . $value . '<br />';
		}
	}
	?>
		<p>Liste des données récupérées en Post :</p>
	<?php
	if (empty($_POST))
		echo 'VIDE!!!';
	else{
		foreach($_POST as $key => $value)
		{
	   	echo '<b>Key</b> = ' . $key . ' / ';
	   	echo '<b>Value</b> = ' . $value . '<br />';
		}
	}
	?>

	</body>
</html>
