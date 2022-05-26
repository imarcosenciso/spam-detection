<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#prerrequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
El proyecto realizado consiste en la exploración e implementación de técnicas para la detección y filtrado de spam mediante técnicas de procesamiento del lenguaje natural, y su objetivo es alcanzar la capacidad de clasificar mensajes entre aquellos que sean spam o no spam. Pero para ello se necesita primero saber qué significa la palabra spam y la situación actual alrededor de este término, además de la propia definición del procesamiento del lenguaje natural o NLP. Así pues, a lo largo de este apartado se explican estos puntos, junto a algunos datos estadísticos sobre el spam y tipos de uso y algoritmos típicos de NLP.

Para entender mejor el alcance del proyecto, leer la [documentación](https://drive.google.com/file/d/1BrQKt97ZFfvzZXb24kC6ivpHUCduqSzk/view?usp=sharing)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE -->
## Usage
El proyecto en su totalidad se ejecuta en Jupyter notebooks. Para su ejecución, es necesario descargar el [dataset inical](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection), guardarlo en la carpeta `Data/dataset` (crearla si no existe) y ejecutar en primer lugar el fichero `preprocessing.ipynb`. Esto creará carpetas y demás documentos dentor de la carpeta de dataset.

A continuación, ejecutar `analisis_algoritmos.ipynb` en la carpeta `src`. Una vez realizado esto, tendremos los modelos y ficheros necesarios para ejecutar `demo.ipynb` y entender cómo funciona.


### Built With
* Jupyer notebook
* Python
* Las siguientes librerías de machine learning y NLP:
    * nltk
    * sklearn
    * scipy
    * gensim
<p align="right">(<a href="#top">back to top</a>)</p>


### Prerequisites
* Se ha utilizado `Python 3.9.7 64-bit`
* Instalar librerías con `pip install -r requirements.txt`
* [Dataset inicial](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection). Ver <a href="##usage">Usage</a>.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Iñigo Marcos - imarcosenciso@opendeusto.es

Project Link: [https://github.com/imarcosenciso/spam-detection](https://github.com/imarcosenciso/spam-detection)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/imarcosenciso/spam-detection.svg?style=for-the-badge
[contributors-url]: https://github.com/imarcosenciso/spam-detection/graphs/contributors
[license-shield]: https://img.shields.io/github/license/imarcosenciso/spam-detection.svg?style=for-the-badge
[license-url]: https://github.com/imarcosenciso/spam-detection/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/i%C3%B1igo-marcos-0a68781b9/

