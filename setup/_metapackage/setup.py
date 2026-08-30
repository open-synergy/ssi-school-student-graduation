import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-school-student-graduation",
    description="Meta package for open-synergy-ssi-school-student-graduation Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_school_student_graduation',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
