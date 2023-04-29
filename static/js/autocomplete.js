$( function() {
    $( "#autocomplete" ).autocomplete({
      source: "/jobs/autocomplete"
    });
  } );

  /* Este código es una función de jQuery que implementa una funcionalidad de autocompletado en un campo
     de entrada de texto llamado "autocomplete". La función espera a que la página termine de cargarse para
     iniciar su ejecución con $( function() {...}) (equivalente a $(document).ready(function() {...})).
     
     Luego, se llama al método autocomplete() de jQuery, pasando como un objeto de configuración que establece
     el origen de los datos a "/jobs/autocomplete". Este es un endpoint que devuelve los valores de
     autocompletado para el campo de entrada cuando se dispara el evento de entrada en el campo.

     En resumen, este código implementa la funcionalidad de autocompletado en un campo de entrada de texto
     específico, con los datos obtenidos de un endpoint específico "/jobs/autocomplete", cuando se dispara
     el evento de entrada en el campo. */