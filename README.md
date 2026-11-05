# pointcloud-time-unit-probe

## Français

Comparer les hypothèses d’unité des horodatages de points.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m pointcloud_time_unit_probe examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Évalue quatre hypothèses d’unité par rapport à la durée déclarée et garde toutes les hypothèses compatibles ; évite de déduire une unité unique d’une simple plage.

### Limites

Aucun décodage PointCloud2 ni conversion appliquée aux données. Une plage compatible ne prouve ni unité ni synchronisation correcte.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compare point timestamp unit hypotheses.

Synthetic data; no network access or secret required.

```sh
python -m pointcloud_time_unit_probe examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Evaluates four unit hypotheses against declared scan duration and retains every compatible hypothesis; avoids inferring a unique unit from a range alone.

### Limits

No PointCloud2 decoding or conversion applied to data. Compatible range proves neither units nor correct synchronization.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comparar hipótesis de unidades de marcas temporales de puntos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m pointcloud_time_unit_probe examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Evalúa cuatro hipótesis de unidad frente a duración declarada y conserva todas las compatibles; evita inferir unidad única de un rango.

### Límites

Sin decodificación PointCloud2 ni conversión de datos. Un rango compatible no prueba unidad ni sincronización correcta.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html
