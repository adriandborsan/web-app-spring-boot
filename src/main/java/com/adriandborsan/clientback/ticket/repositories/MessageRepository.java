package com.adriandborsan.clientback.ticket.repositories;

import com.adriandborsan.clientback.ticket.entities.TicketMessage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;


@Repository
public interface MessageRepository extends JpaRepository<TicketMessage, Long> {
    List<TicketMessage> findByTicketId(Long ticketId);
}
