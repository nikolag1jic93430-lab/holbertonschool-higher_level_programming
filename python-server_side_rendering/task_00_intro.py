import os

def generate_invitations(template, attendees):
    # 1. Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
        
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Gestion des entrées vides
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
        
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 3. Traitement de chaque participant
    for index, attendee in enumerate(attendees, start=1):
        invitation_content = template
        
        # Liste des variables attendues dans le template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            # Récupérer la valeur. get() renvoie None si la clé n'existe pas.
            value = attendee.get(placeholder)
            
            # Si la donnée est manquante ou vaut None, on met "N/A"
            if value is None:
                value = "N/A"
            
            # Remplacement dans le texte (ex: "{name}" -> "Alice")
            invitation_content = invitation_content.replace(f"{{{placeholder}}}", str(value))
        
        # 4. Génération des fichiers de sortie
        output_filename = f"output_{index}.txt"
        
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation_content)
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")