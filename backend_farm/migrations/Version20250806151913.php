<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20250806151913 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql(<<<'SQL'
            ALTER TABLE category ADD image VARCHAR(255) NOT NULL
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE module ADD CONSTRAINT FK_C24262812469DE2 FOREIGN KEY (category_id) REFERENCES category (id)
        SQL);
        $this->addSql(<<<'SQL'
            CREATE INDEX IDX_C24262812469DE2 ON module (category_id)
        SQL);
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql(<<<'SQL'
            ALTER TABLE category DROP image
        SQL);
        $this->addSql(<<<'SQL'
            ALTER TABLE module DROP FOREIGN KEY FK_C24262812469DE2
        SQL);
        $this->addSql(<<<'SQL'
            DROP INDEX IDX_C24262812469DE2 ON module
        SQL);
    }
}
