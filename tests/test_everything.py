from template.models import PersonModel

def test_model(db_session):
    person = PersonModel(name='someone',
                    email='something@something.com')
    
    db_session.add(person)
    db_session.commit()

    post_person = db_session.query(PersonModel).filter(PersonModel.name == 'someone').first()

    assert post_person.email == 'something@something.com'
