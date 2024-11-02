# Project for INF5001

This project calculate billable time by recursively searching through user selected folder efficiently.

La spectroscopie de résonance magnétique nucléaire permet de sonder la matière à l’échelle de l’Ånsgtröm (1 x 10-10 m), c’est un outil essentiel à l’interface entre la physique et la chimie. Les chimistes de synthèse notamment y ont recours plusieurs fois par jour. Le département de chimie de l’UQAM possède trois appareils de ce type. 

La maintenance de ces appareils coûtant plusieurs milliers de dollars par année, les groupes de recherche payent des frais d’usagers. Le montant payé est fonction du temps d’utilisation de l’appareil. Ce temps d’utilisation est enregistré dans un fichier texte dans lequel sont indiqués les heures exactes de début et de fin de chaque expérience. Ce fichier texte est placé dans un répertoire dans une arborescence de type : Groupe_de_recherche/nom_de_l’Expérience/Numéro_de_l’expérience/. La facturation étant faite une fois par semestre, il peut y avoir plusieurs centaines d’expériences enregistrées par groupe de recherche. 

Le but du projet est d’écrire une script dans un langage comme Python qui cherche et somme les durées de toutes les expériences enregistrées par un groupe de recherche entre deux dates fixées par l’utilisateur. Le script devra être fonctionnel sous Windows 7, 10 et 11. 

En plus de faciliter la facturation - un besoin réel au département de chimie - le projet pourrait être facilement adaptable à d’autres situations où la durée d’une activité spécifique – soit-elle commerciale ou privée - a besoin d’être comptabilisée. 
